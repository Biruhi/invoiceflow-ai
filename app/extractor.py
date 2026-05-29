import fitz


def extract_text_from_pdf(pdf_path):

    text = ""

    pdf = fitz.open(pdf_path)

    for page in pdf:

        text += page.get_text()

    return text


def extract_pages(pdf_path):

    pdf = fitz.open(pdf_path)

    pages = []

    for page in pdf:

        pages.append(
            page.get_text()
        )

    return pages