FROM python:3.8-slim

WORKDIR /app

# Install dependencies dasar
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Salin seluruh isi folder projek
COPY . .

# Jalankan Rasa dengan mendengarkan port dari lingkungan ($PORT)
CMD ["sh", "-c", "rasa run --enable-api --cors '*' --port $PORT --keep-response-listeners"]
