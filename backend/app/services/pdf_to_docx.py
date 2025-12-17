import subprocess
import tempfile
import os
from io import BytesIO

async def docx_to_pdf_stream(file) -> tuple[BytesIO, str]:
    # Leer bytes del archivo subido
    docx_bytes = await file.read()

    # Guardar DOCX en archivo temporal
    temp_dir = tempfile.mkdtemp()
    docx_path = os.path.join(temp_dir, file.filename)
    with open(docx_path, "wb") as f:
        f.write(docx_bytes)

    # Ruta de salida PDF
    pdf_path = docx_path.replace(".docx", ".pdf")

    # Ejecutar Pandoc para convertir DOCX → PDF
    subprocess.run(
        ["pandoc", docx_path, "-o", pdf_path],
        check=True
    )

    # Leer PDF generado en memoria
    with open(pdf_path, "rb") as f:
        pdf_bytes = f.read()

    pdf_stream = BytesIO(pdf_bytes)
    pdf_stream.seek(0)

    return pdf_stream, os.path.basename(pdf_path)