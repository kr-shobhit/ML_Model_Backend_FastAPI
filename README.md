# ML Deployment Suite: FastAPI & Streamlit Integration

This repository contains a full-stack implementation for serving and interacting with a Machine Learning model. The project demonstrates a robust **MLOps pipeline** by integrating a high-performance **FastAPI** backend with an interactive **Streamlit** frontend.

## 🎯 Project Goal
The primary objective of this project is to bridge the gap between model training and production deployment. It wraps a pre-trained machine learning model in a production-grade API and provides a user-friendly web interface for real-time predictions.

---

## 🚀 Key Features
* **Real-time Prediction:** Instant model inference via API.
* **Interactive UI:** User-friendly form for data entry using Streamlit.
* **Data Validation:** Robust input validation using Pydantic models.
* **Containerized:** Fully Dockerized for easy deployment and scalability.
* **API Documentation:** Automatic interactive swagger documentation.

---

## 🛠️ Tech Stack

* **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
* **Web Server:** [Uvicorn](https://www.uvicorn.org/)
* **Data Validation:** [Pydantic](https://docs.pydantic.dev/)
* **Frontend:** [Streamlit](https://streamlit.io/)
* **Containerization:** [Docker](https://www.docker.com/) & Docker Compose

---


## 📦 Running Project 

If you prefer to run the application, follow these steps. You will need **two separate terminal windows** (one for the backend, one for the frontend).

### 1. Setup Environment
```bash
git clone https://github.com/kr-shobhit/ML_Model_Backend_FastAPI.git
```

```bash
cd ML_Model_Backend_FastAPI
```

### 2. Create Virtual Environment

```bash
python -m venv .venv        # For Windows
```

```bash
# python3 -m venv .venv     # For Mac/Linux
```

### 3. Activate Virtual Environment

```bash
.venv\Scripts\activate      # Windows
```

```bash
source .venv/bin/activate # Mac/Linux
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run Project
Note: This will require two indivisual terminals to run frontend and backend of the project.

```bash
uvicorn main:app --reload
```
The backend is now running at `http://127.0.0.1:8000` .

```bash
cd frontend
streamlit run visual.py
```
The frontend should automatically open in your browser at `http://localhost:8501` .

---

## Folder Structure

```bash
├── frontend/
│   └── visual.py          # Streamlit application
├── model/
│   ├── model.pkl          # Pre-trained ML model
│   └── trained_model.ipynb # Model training notebook
├── validation/
│   └── data_validation.py # Pydantic schemas
├── dataset/               # Raw data files
├── main.py                # FastAPI backend entry point
├── requirements.txt       # Python dependencies
├── Dockerfile.backend     # Backend Docker configuration
├── Dockerfile.frontend    # Frontend Docker configuration
├── docker-compose.yml     # Docker orchestration
└── README.md              # Project documentation
```

---

## 🤝 Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

1. Fork the Project
2. Create your Feature Branch `(git checkout -b feature/AmazingFeature)`
3. Commit your Changes `(git commit -m 'Add some AmazingFeature')`
4. Push to the Branch `(git push origin feature/AmazingFeature)`
5. Open a Pull Request

## 📝 License
Distributed under the MIT License. See `LICENSE` for more information.
