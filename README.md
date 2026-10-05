
# Rasa Guitar Chatbot (v3.5.0)

[![Rasa Open Source](https://img.shields.io/badge/Rasa-3.5.0-purple.svg)](https://rasa.com/)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

I am experimenting with Rasa 3.5.0 to build a simple bot for asking about guitar chords. This is an interactive text-based chatbot built using the **Rasa Open Source (v3.5.0)** framework to handle Natural Language Understanding (NLU) and dialogue management locally.

---

## 📌 Key Features

- **Intent Recognition & Entity Extraction**: Capable of understanding user intents and extracting important data variables.
- **Custom Actions**: Custom business logic and external integrations powered by the Python SDK (`rasa-sdk`), specifically used to fetch and display ASCII guitar chords.
- **Local Deployment**: Runs completely in a local environment without relying on paid external APIs.

---

## 🛠️ Tech Stack & Prerequisites

- **Python**: v3.10.x *(Virtual Environment strongly recommended)*
- **Rasa Open Source**: v3.5.0
- **Rasa SDK**: v3.5.x

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/username/nama-repo-bot.git](https://github.com/username/nama-repo-bot.git)
cd nama-repo-bot

```

### 2. Create & Activate Virtual Environment

```bash
python -m venv venv

# Activate on Windows:
.\venv\Scripts\activate

# Activate on Linux / macOS:
source venv/bin/activate

```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt

```

### 4. Train the Model

```bash
rasa train

```

### 5. Run the Chatbot

Open two separate terminal windows:

**Terminal 1 (Action Server):**

```bash
rasa run actions

```

**Terminal 2 (Interactive Shell / API):**

```bash
# To run in the terminal:
rasa shell

# OR, to connect with the FrontendBot (HTML/CSS UI), run this instead:
rasa run -cors * --enable-api -p 10000

```

*(If using the Frontend UI, simply open `FrontendBot/index.html` via a local server extension like VS Code Live Server).*

---

## 📊 Model Evaluation

![DIETClassifier Confusion Matrix](results/DIETClassifier_confusion_matrix.png)

## 📂 Project Structure

```text
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

```

> **Important Note:** Configuration files such as `Dockerfile` and `Procfile` in this repository are provided as optional deployment preparations and are currently in the experimental stage (untested).

---

## 📜 License

This project is built using Rasa Open Source v3.5.0 and is licensed under the [Apache License 2.0](https://opensource.org/licenses/Apache-2.0).
