from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
import base64
import os

from src.extract_text import extract_text
from src.summarize import summarize_text
from src.entities import extract_entities
from src.sentiment import get_sentiment

app = FastAPI()

API_KEY = "sk_track2_987654321"

class DocumentRequest(BaseModel):
    fileName: str
    fileType: str
    fileBase64: str

@app.post("/api/document-analyze")
def analyze_document(request: DocumentRequest, x_api_key: str = Header(None)):

    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

    try:
        # Fix Base64 padding
        file_base64 = request.fileBase64
        file_base64 += "=" * (-len(file_base64) % 4)

        # Decode Base64
        file_data = base64.b64decode(file_base64)
        file_path = f"temp_{request.fileName}"

        with open(file_path, "wb") as f:
            f.write(file_data)

        # Extract text
        text = extract_text(file_path, request.fileType)

        # NLP
        summary = summarize_text(text)
        entities = extract_entities(text)
        sentiment = get_sentiment(text)

        # Delete temp file
        os.remove(file_path)

        return {
            "status": "success",
            "fileName": request.fileName,
            "summary": summary,
            "entities": entities,
            "sentiment": sentiment
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
