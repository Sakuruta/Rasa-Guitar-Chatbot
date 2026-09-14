FROM python:3.8-slim

WORKDIR /app

# Install dependencies dasar
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Salin seluruh isi folder projek
COPY . .

# Jalankan server Rasa API secara resmi tanpa argumen workers
CMD ["rasa", "run", "--enable-api", "--cors", "*", "--port", "8000"]
