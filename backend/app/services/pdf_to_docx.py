import tempfile
import os
from pdf2docx import Converter

def pdf_to_docx_stream(upload_file):
    """
    Convierte un archivo PDF recibido como UploadFile en un DOCX temporal.
    Retorna la ruta del archivo DOCX generado.
    """

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_pdf:
        upload_file.file.seek(0)
        tmp_pdf.write(upload_file.file.read())
        tmp_pdf_path = tmp_pdf.name

    tmp_docx_path = tmp_pdf_path.replace(".pdf", ".docx")

    try:
        cv = Converter(tmp_pdf_path)
        cv.convert(tmp_docx_path, start=0, end=None)
        cv.close()
        return tmp_docx_path

    except Exception as e:
        raise RuntimeError(f"Error al convertir PDF a DOCX: {e}")

    finally:
        if os.path.exists(tmp_pdf_path):
            os.remove(tmp_pdf_path)