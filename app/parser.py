import re


def clean_money(value):

    if not value:
        return ""

    return value.replace(",", "")


def parse_invoice(text):

    invoice_number = ""
    vendor = ""
    customer = ""
    invoice_date = ""
    due_date = ""
    subtotal = ""
    tax = ""
    total = ""
    currency = "USD"

    # =====================
    # INVOICE NUMBER
    # =====================

    match = re.search(
        r"Invoice Number:\s*([A-Za-z0-9\-]+)",
        text,
        re.IGNORECASE
    )

    if match:

        invoice_number = match.group(1)

    # =====================
    # VENDOR
    # =====================

    match = re.search(
        r"Vendor:\s*(.+)",
        text
    )

    if match:

        vendor = match.group(1).strip()

    # =====================
    # CUSTOMER
    # =====================

    match = re.search(
        r"Customer:\s*(.+)",
        text
    )

    if match:

        customer = match.group(1).strip()

    # =====================
    # INVOICE DATE
    # =====================

    match = re.search(
        r"(?:Invoice Date|Date):\s*(\d{2}/\d{2}/\d{4})",
        text
    )

    if match:

        invoice_date = match.group(1)

    # =====================
    # DUE DATE
    # =====================

    match = re.search(
        r"Due Date:\s*(\d{2}/\d{2}/\d{4})",
        text
    )

    if match:

        due_date = match.group(1)

    # =====================
    # SUBTOTAL
    # =====================

    match = re.search(
        r"Subtotal:\s*\$?([\d,]+\.\d{2})",
        text,
        re.IGNORECASE
    )

    if match:

        subtotal = clean_money(
            match.group(1)
        )

    # =====================
    # TAX
    # =====================

    match = re.search(
        r"Tax.*?:\s*\$?([\d,]+\.\d{2})",
        text,
        re.IGNORECASE
    )

    if match:

        tax = clean_money(
            match.group(1)
        )

    # =====================
    # TOTAL
    # =====================

    total_patterns = [

        r"Amount Due:\s*\$?([\d,]+\.\d{2})",

        r"Grand Total:\s*\$?([\d,]+\.\d{2})",

        r"Total:\s*\$?([\d,]+\.\d{2})"
    ]

    for pattern in total_patterns:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:

            total = clean_money(
                match.group(1)
            )

            break

    return {

        "Invoice Number":
        invoice_number,

        "Vendor":
        vendor,

        "Customer":
        customer,

        "Invoice Date":
        invoice_date,

        "Due Date":
        due_date,

        "Subtotal":
        subtotal,

        "Tax":
        tax,

        "Total":
        total,

        "Currency":
        currency
    }