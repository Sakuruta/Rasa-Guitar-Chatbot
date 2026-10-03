FROM python:3.8-slim

WORKDIR /app

# Install dependencies dasar
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Salin seluruh isi folder projek
COPY . .

# Gunakan exec form agar variabel $PORT terbaca dengan benar
CMD ["sh", "-c", "rasa run --enable-api --cors '*' -p ${PORT:-5005}"]
