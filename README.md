# Rasa Guitar Chatbot (v3.5.0)

[![Rasa Open Source](https://img.shields.io/badge/Rasa-3.5.0-purple.svg)](https://rasa.com/)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Saya mencoba Rasa 3.5.0 membuat bot simple untuk bertanya tentang chord gitar
Bot interaktif berbasis teks yang dibangun menggunakan framework **Rasa Open Source (v3.5.0)** untuk menangani pemrosesan bahasa alami (NLU) dan manajemen dialog secara lokal.

---

## 📌 Fitur Utama

- **Intent Recognition & Entity Extraction**: Mampu memahami maksud pesan pengguna dan mengambil variabel data penting.
- **Custom Actions**: Logika kustom dan integrasi eksternal berbasis Python SDK (`rasa-sdk`). digunakan untuk mengambil chord ascii
- **Local Deployment**: Berjalan sepenuhnya di lingkungan lokal tanpa tergantung pada API luar berbayar.

---

## 🛠️ Teknologi & Prasyarat

- **Python**: v3.8 atau v3.9 *(disarankan memakai Virtual Environment)*
- **Rasa Open Source**: v3.5.0
- **Rasa SDK**: v3.5.x

---

## ⚙️ Cara Instalasi & Penggunaan

### 1. Clone Repositori
git clone [https://github.com/username/nama-repo-bot.git](https://github.com/username/nama-repo-bot.git)
cd nama-repo-bot

### 2. Buat & Aktifkan Virtual Environment
python -m venv venv

# Mengaktifkan di Windows:
.\venv\Scripts\activate

# Mengaktifkan di Linux / macOS:
source venv/bin/activate

### 3. Instal Dependensi
pip install --upgrade pip
pip install rasa==3.5.0

### 4. Pelatihan Model (Training)
rasa train

### 5. Jalankan Chatbot
# Terminal 1:
rasa run actions

# Terminal 2:
rasa shell

---

## 📊 Model Evaluation
![DIETClassifier Confusion Matrix](results/DIETClassifier_confusion_matrix.png)


## 📂 Struktur Folder Proyek

Rasa-Bot/
├── actions/
│   └── actions.py              # Custom action logic (Python)
├── data/
│   ├── nlu.yml                 # NLU training data (intents & entities)
│   ├── rules.yml               # Fixed rule-based dialogue paths
│   └── stories.yml             # Dialogue training stories
├── FrontendBot/
│   ├── index.html              # Web chat layout & structure
│   └── style.css               # Styling and responsive design
├── results/                    # Model evaluation reports & confusion matrices
├── config.yml                  # NLU pipeline & policy configuration
├── domain.yml                  # Intent, entity, slot, and response definitions
├── credentials.yml             # Channel / integration settings (REST channel)
├── endpoints.yml               # Endpoint configurations (action server)
├── requirements.txt            # Python dependencies
├── runtime.txt                 # Target Python runtime environment
├── Dockerfile                  # Container configuration (Experimental)
├── Procfile                    # Deployment configuration (Experimental)
└── README.md                   # Project documentation

Catatan Penting: File konfigurasi seperti Dockerfile di repositori ini disediakan sebagai persiapan deployment opsional dan saat ini masih dalam tahap eksperimen (belum diuji penuh).

---

## 📜 Lisensi

Proyek ini dibangun menggunakan Rasa Open Source v3.5.0 yang dilesensikan di bawah Apache License 2.0.
