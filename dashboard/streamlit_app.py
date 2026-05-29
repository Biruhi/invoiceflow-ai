import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

import streamlit as st
import pandas as pd
import plotly.express as px

from app.extractor import (
    extract_pages
)

from app.invoice_detector import (
    detect_invoices
)

from app.parser import (
    parse_invoice
)

from app.analytics import (
    generate_analytics
)

from app.exporter import (
    export_to_excel
)


# ==================================
# PAGE CONFIG
# ==================================

st.set_page_config(
    page_title="InvoiceFlow Enterprise",
    layout="wide"
)

st.title(
    "🧾 InvoiceFlow Enterprise"
)

st.markdown(
    """
    Upload invoice PDFs and automatically
    extract invoice information.
    """
)

# ==================================
# FILE UPLOAD
# ==================================

uploaded_files = st.file_uploader(
    "Upload Invoice PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

# ==================================
# PROCESS FILES
# ==================================

if uploaded_files:

    invoices = []

    os.makedirs(
        "uploads",
        exist_ok=True
    )

    os.makedirs(
        "outputs",
        exist_ok=True
    )

    for uploaded_file in uploaded_files:

        pdf_path = (
            f"uploads/{uploaded_file.name}"
        )

        with open(
            pdf_path,
            "wb"
        ) as file:

            file.write(
                uploaded_file.read()
            )

        # ==========================
        # EXTRACT PAGES
        # ==========================

        pages = extract_pages(
            pdf_path
        )

        # ==========================
        # DETECT INVOICES
        # ==========================

        invoice_blocks = (
            detect_invoices(
                pages
            )
        )

        # ==========================
        # PARSE EACH INVOICE
        # ==========================

        for invoice_text in invoice_blocks:

            invoice_data = (
                parse_invoice(
                    invoice_text
                )
            )

            invoices.append(
                invoice_data
            )

    # ==========================
    # DATAFRAME
    # ==========================

    df = pd.DataFrame(
        invoices
    )

    # Remove duplicate invoices

    if "Invoice Number" in df.columns:

        df = df.drop_duplicates(
            subset=[
                "Invoice Number"
            ]
        )

    # Numeric columns

    for column in [

        "Subtotal",
        "Tax",
        "Total"

    ]:

        if column in df.columns:

            df[column] = pd.to_numeric(
                df[column],
                errors="coerce"
            ).fillna(0)

    # ==========================
    # ANALYTICS
    # ==========================

    analytics = (
        generate_analytics(
            df
        )
    )

    # ==========================
    # KPI DASHBOARD
    # ==========================

    st.subheader(
        "📊 Dashboard"
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Invoices",
        analytics["Invoice Count"]
    )

    col2.metric(
        "Vendors",
        analytics["Vendor Count"]
    )

    col3.metric(
        "Total Spend",
        f"${analytics['Total Spend']:,.2f}"
    )

    col4.metric(
        "Average Invoice",
        f"${analytics['Average Invoice']:,.2f}"
    )

    # ==========================
    # INVOICE TABLE
    # ==========================

    st.subheader(
        "📋 Invoice Records"
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    # ==========================
    # SPEND BY VENDOR
    # ==========================

    st.subheader(
        "📈 Spend by Vendor"
    )

    vendor_df = (
        df.groupby(
            "Vendor",
            as_index=False
        )["Total"]
        .sum()
    )

    vendor_chart = px.bar(
        vendor_df,
        x="Vendor",
        y="Total",
        title="Spend by Vendor",
        text="Total"
    )

    vendor_chart.update_traces(
        texttemplate="$%{text:,.2f}",
        textposition="outside"
    )

    st.plotly_chart(
        vendor_chart,
        use_container_width=True
    )

    # ==========================
    # VENDOR LEADERBOARD
    # ==========================

    st.subheader(
        "🏆 Vendor Leaderboard"
    )

    leaderboard = (
        vendor_df
        .sort_values(
            by="Total",
            ascending=False
        )
        .copy()
    )

    leaderboard["Total"] = (
        "$" +
        leaderboard["Total"]
        .map(
            lambda x:
            f"{x:,.2f}"
        )
    )

    st.dataframe(
        leaderboard,
        use_container_width=True
    )

    # ==========================
    # INVOICE DETAILS
    # ==========================

    st.subheader(
        "🏢 Invoice Details"
    )

    selected_invoice = st.selectbox(
        "Select Invoice",
        df["Invoice Number"]
    )

    selected_row = df[
        df["Invoice Number"]
        ==
        selected_invoice
    ]

    if len(selected_row) > 0:

        invoice = (
            selected_row
            .iloc[0]
        )

        st.write(
            f"**Invoice Number:** {invoice['Invoice Number']}"
        )

        st.write(
            f"**Vendor:** {invoice['Vendor']}"
        )

        st.write(
            f"**Customer:** {invoice['Customer']}"
        )

        st.write(
            f"**Invoice Date:** {invoice['Invoice Date']}"
        )

        st.write(
            f"**Due Date:** {invoice['Due Date']}"
        )

        st.write(
            f"**Subtotal:** ${invoice['Subtotal']:,.2f}"
        )

        st.write(
            f"**Tax:** ${invoice['Tax']:,.2f}"
        )

        st.write(
            f"**Total:** ${invoice['Total']:,.2f}"
        )

        st.write(
            f"**Currency:** {invoice['Currency']}"
        )

    # ==========================
    # EXCEL EXPORT
    # ==========================

    output_file = (
        "outputs/invoice_report.xlsx"
    )

    export_to_excel(
        df,
        output_file
    )

    with open(
        output_file,
        "rb"
    ) as file:

        st.download_button(
            label=
            "⬇ Download Excel Report",
            data=file,
            file_name=
            "invoice_report.xlsx",
            mime=
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )