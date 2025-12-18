# ML Deployment Suite: FastAPI & Streamlit Integration

This repository contains a full-stack implementation for serving and interacting with a Machine Learning model. The project focuses on building a robust **FastAPI** backend and an interactive **Streamlit** frontend to handle user data, perform real-time feature engineering, and return model predictions.

## 🎯 Project Goal
The primary objective of this project was to master the **MLOps pipeline**—specifically how to take a pre-trained model and wrap it in a production-grade API while providing a user-friendly interface.

---

## 🛠️ Tech Stack

* **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
* **Web Server:** [Uvicorn](https://www.uvicorn.org/)
* **Data Validation:** [Pydantic](https://docs.pydantic.dev/)
* **Frontend:** [Streamlit](https://streamlit.io/)

---

## 📦 Installation & Setup

1. Clone the Repository
```bash
git clone https://github.com/kr-shobhit/ML_Model_Backend_FastAPI.git
```
```bash
cd your-repo-name
```
2. Install Dependencies
```bash
pip install requirements.txt
```
3. Start the Backend (FastAPI):
```bash
uvicorn main:app --reload
```
4. Start the Frontend (Streamlit):
```bash
streamlit run app.py
```
5. You can also visit the interactive API documentation at ```http://127.0.0.1:8000/docs```

---
