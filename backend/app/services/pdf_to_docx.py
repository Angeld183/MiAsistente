# backend/app/services/pdf_to_docx.py
import subprocess
import tempfile
import os
from io import BytesIO

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

    # Ejecutar Pandoc para convertir PDF → DOCX
    subprocess.run(
        ["pandoc", pdf_path, "-o", docx_path],
        check=True
    )

    # Leer DOCX generado en memoria
    with open(docx_path, "rb") as f:
        docx_bytes = f.read()

    docx_stream = BytesIO(docx_bytes)
    docx_stream.seek(0)

    return docx_stream, os.path.basename(docx_path)