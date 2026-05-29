import pandas as pd


def export_to_excel(
    df,
    output_path
):

    with pd.ExcelWriter(
        output_path,
        engine="openpyxl"
    ) as writer:

        df.to_excel(
            writer,
            index=False,
            sheet_name="Invoices"
        )

    return output_path