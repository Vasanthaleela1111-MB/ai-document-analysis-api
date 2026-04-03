import PyPDF2
import docx
import pytesseract
from PIL import Image
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
def extract_text(file_path, file_type):
    text = ""

    if file_type == "pdf":
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text()

    elif file_type == "docx":
        doc = docx.Document(file_path)
        for para in doc.paragraphs:
            text += para.text

    elif file_type == "image":
        img = Image.open(file_path)
        text = pytesseract.image_to_string(img)

    return text
