# app/services/docx_to_pdf.py
from docx2pdf import convert
from io import BytesIO
import tempfile
import os

async def docx_to_pdf_stream(file) -> tuple[BytesIO, str]:
    # Leer bytes del archivo subido
    docx_bytes = await file.read()

    # Crear archivo temporal .docx
    temp_dir = tempfile.mkdtemp()
    docx_path = os.path.join(temp_dir, file.filename)
    with open(docx_path, "wb") as f:
        f.write(docx_bytes)

    # Crear ruta de salida .pdf
    pdf_path = docx_path.replace(".docx", ".pdf")

    # Convertir DOCX → PDF
    convert(docx_path, pdf_path)

    # Leer el PDF generado en memoria
    with open(pdf_path, "rb") as f:
        pdf_bytes = f.read()

    pdf_stream = BytesIO(pdf_bytes)
    pdf_stream.seek(0)

    return pdf_stream, os.path.basename(pdf_path)