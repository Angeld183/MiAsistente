import tempfile
import os
from io import BytesIO
from pdf2docx import Converter

async def pdf_to_docx_stream(file) -> tuple[BytesIO, str]:
    # Leer bytes del archivo subido
    pdf_bytes = await file.read()

    # Guardar PDF en archivo temporal
    temp_dir = tempfile.mkdtemp()
    pdf_path = os.path.join(temp_dir, file.filename)
    with open(pdf_path, "wb") as f:
        f.write(pdf_bytes)

    # Ruta de salida DOCX
    docx_path = pdf_path.replace(".pdf", ".docx")

    # Convertir PDF → DOCX usando pdf2docx
    cv = Converter(pdf_path)
    cv.convert(docx_path, start=0, end=None)
    cv.close()

    # Leer DOCX generado en memoria
    with open(docx_path, "rb") as f:
        docx_bytes = f.read()

    docx_stream = BytesIO(docx_bytes)
    docx_stream.seek(0)

    return docx_stream, os.path.basename(docx_path)