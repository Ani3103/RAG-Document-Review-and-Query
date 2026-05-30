from pypdf import PdfReader
import io


def extract_text_from_pdf(file_bytes):
    reader = PdfReader(io.BytesIO(file_bytes))

    text = ""

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted

    return text