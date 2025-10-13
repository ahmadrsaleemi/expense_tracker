FROM python:3.11-slim-bookworm

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        tesseract-ocr \
        libtesseract-dev \
        libleptonica-dev \
        pkg-config && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir Flask==3.0.0 pytesseract Pillow gunicorn python-dotenv

COPY . .

EXPOSE 5000

ENV FLASK_APP=run.py

ENV FLASK_RUN_HOST=0.0.0.0

CMD ["gunicorn", "-b", "0.0.0.0:5000", "run:app"]