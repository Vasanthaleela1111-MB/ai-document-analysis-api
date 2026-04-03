import PyPDF2
import docx
import pytesseract
from PIL import Image
import os

def extract_text(file_path, file_type):
    text = ""

    try:
        # PDF Extraction
        if file_type == "pdf":
            with open(file_path, "rb") as file:
                reader = PyPDF2.PdfReader(file)
                for page in reader.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text

            # If PDF has no text (scanned PDF), try OCR
            if text.strip() == "":
                try:
                    from pdf2image import convert_from_path
                    images = convert_from_path(file_path)
                    for img in images:
                        text += pytesseract.image_to_string(img)
                except:
                    pass

        # DOCX Extraction
        elif file_type == "docx":
            doc = docx.Document(file_path)
            for para in doc.paragraphs:
                text += para.text + "\n"

        # Image OCR
        elif file_type == "image":
            img = Image.open(file_path)
            text = pytesseract.image_to_string(img)

        else:
            text = "Unsupported file type"

    except Exception as e:
        text = "Error extracting text: " + str(e)

    return text
