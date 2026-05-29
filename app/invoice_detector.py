import re


def detect_invoices(pages):

    full_text = "\n".join(
        pages
    )

    invoice_chunks = re.split(

        r"(?=Invoice Number:)",

        full_text,

        flags=re.IGNORECASE
    )

    invoices = []

    for chunk in invoice_chunks:

        chunk = chunk.strip()

        if len(chunk) > 50:

            invoices.append(
                chunk
            )

    return invoices