# Etapa de backend con Python
FROM python:3.12-slim AS backend
WORKDIR /app

# Dependencias del backend
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y pandoc texlive-latex-base texlive-xetex texlive-fonts-recommended

# Copiar código del backend
COPY backend/app ./app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]