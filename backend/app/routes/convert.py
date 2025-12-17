from fastapi import UploadFile, File, HTTPException, APIRouter
from fastapi.responses import FileResponse
from app.services.pdf_to_docx import pdf_to_docx_stream
from app.services.docx_to_pdf import docx_to_pdf_stream

router = APIRouter()

@router.post("/pdf-to-docx")
async def pdf_to_docx(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Tipo de archivo no permitido. Se requiere PDF.")
    try:
        # Llamada síncrona al servicio
        docx_path = pdf_to_docx_stream(file)

        return FileResponse(
            docx_path,
            media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            filename=file.filename.replace(".pdf", ".docx")
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al convertir PDF a DOCX: {str(e)}")


@router.post("/docx-to-pdf")
async def docx_to_pdf(file: UploadFile = File(...)):
    if file.content_type not in [
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "application/msword"  # por si algunos envían .doc
    ]:
        raise HTTPException(status_code=400, detail="Tipo de archivo no permitido. Se requiere DOCX/DOC.")
    try:
        # Llamada síncrona al servicio
        pdf_path = docx_to_pdf_stream(file)

        return FileResponse(
            pdf_path,
            media_type="application/pdf",
            filename=file.filename.replace(".docx", ".pdf")
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al convertir DOCX a PDF: {str(e)}")