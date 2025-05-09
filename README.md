# Backend Analyzer
A developer-first tool to track, log, and visualize API request activity in real-time using FastAPI and Streamlit.

##📚 Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Screenshots](#screenshots)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

  ## 📖 About the Project

Backend Analyzer is designed for backend developers and cloud engineers who want visibility into how their APIs are being used. It intercepts and logs requests made to your 
FastAPI endpoints, stores them in a database, and presents real-time visual analytics using Streamlit.

## ✨ Features

- 📊 Real-time request logging
- 🧠 Built with FastAPI middleware
- 🗃️ Stores logs in a relational DB
- 📈 Interactive Streamlit dashboard
- 🔎 Filter by endpoint, status, date
- 🧪 Extensible for error tracking or auth analysis

## 🧰 Tech Stack

- **Backend:** FastAPI
- **Dashboard:** Streamlit
- **Database:** SQLite / PostgreSQL
- **ORM:** SQLAlchemy
- **Data Viz:** Plotly / Altair
- **Language:** Python 3.10+

  📸 6. Screenshots

  ## ⚙️ Getting Started

### 🔧 Prerequisites
- Python 3.10+
- pip

### 📦 Installation

```bash
git clone https://github.com/your-username/backend-analyzer.git
cd backend-analyzer
pip install -r requirements.txt

uvicorn app.main:app --reload
cd dashboard
streamlit run Home.py
yaml
Copy
Edit
### 🧭 8. **Usage**
```markdown
## 🧭 Usage

1. Launch your FastAPI server.
2. Make API requests to your backend.
3. Watch them appear in real time on your Streamlit dashboard.

## 🗂️ Folder Structure
backend-analyzer/
│
├── app/
│ ├── main.py
│ ├── middleware/
│ ├── models/
│ ├── crud/
│ ├── config.py
│ └── database.py
│
├── dashboard/
│ ├── Home.py
│ ├── pages/
│ └── utils/
│
├── tests/
├── .env
├── requirements.txt
└── README.md
