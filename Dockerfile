FROM python:3.8-slim

WORKDIR /app

# Install dependencies dasar
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Salin seluruh isi folder projek (termasuk folder models/ yang sudah di-train)
COPY . .

# Jalankan Rasa menggunakan port dinamis dari Render dan batasi pekerja agar hemat RAM
CMD rasa run --enable-api --cors "*" --port $PORT --workers 1
