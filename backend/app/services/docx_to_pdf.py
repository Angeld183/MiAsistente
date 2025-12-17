# app/routes/conversion.py
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import StreamingResponse
from app.services.docx_to_pdf import docx_to_pdf_stream

router = APIRouter()

@router.post("/convert/docx-to-pdf")
async def convert_docx_to_pdf(file: UploadFile = File(...)):
    pdf_stream, filename = await docx_to_pdf_stream(file)
    return StreamingResponse(
        pdf_stream,
        media_type="application/pdf",
        headers={
            "Content-Disposition": f"attachment; filename={filename}"
        }
    )