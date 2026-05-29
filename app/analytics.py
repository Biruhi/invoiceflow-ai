import pandas as pd


def generate_analytics(df):

    if len(df) == 0:

        return {

            "Invoice Count": 0,
            "Vendor Count": 0,
            "Total Spend": 0,
            "Average Invoice": 0
        }

    totals = pd.to_numeric(
        df["Total"],
        errors="coerce"
    ).fillna(0)

    return {

        "Invoice Count":
        len(df),

        "Vendor Count":
        df["Vendor"].nunique(),

        "Total Spend":
        totals.sum(),

        "Average Invoice":
        totals.mean()
    }