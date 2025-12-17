from fastapi import UploadFile, File, HTTPException, APIRouter
from fastapi.responses import StreamingResponse
from app.services.pdf_to_docx import pdf_to_docx_stream
from app.services.docx_to_pdf import docx_to_pdf_stream

router = APIRouter()

@router.post("/pdf-to-docx")
async def pdf_to_docx(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Tipo de archivo no permitido. Se requiere PDF.")
    try:
        docx_stream, filename = await pdf_to_docx_stream(file)
        return StreamingResponse(
            docx_stream,
            media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            headers={"Content-Disposition": f"attachment; filename={filename}"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al convertir PDF a DOCX: {str(e)}")