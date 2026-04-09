# 💧 Groundwater Risk Intelligence System

AI-powered platform to predict groundwater contamination risk, cluster villages, identify top pollutants, and estimate possible health risks using Machine Learning.

---

# 🚀 Live Demo

### 🌐 Streamlit App
https://groundwater-contamination-api-v4v6q3bjmx3mglzpww7xqc.streamlit.app

### ⚡ FastAPI Endpoint
https://groundwater-contamination-api.onrender.com

### 📘 API Docs
https://groundwater-contamination-api.onrender.com/docs

---

# ✨ Features

- ML-based groundwater risk prediction  
- Village-level contamination intelligence  
- Risk classification (Low / Medium / High)  
- Top contaminant ranking  
- Disease risk prediction (health-aware AI)  
- Agglomerative clustering for zone detection  
- Explainable contaminant-based risk reasoning  
- FastAPI production REST API  
- Streamlit interactive dashboard  
- Cloud deployment (Render + Streamlit Cloud)  
- Fully modular ML pipeline  

---

# 🧠 What This System Does

**Input:** Village name  

**Output:**
- Risk level  
- Cluster zone  
- Top contaminants  
- Possible health risks  

Example:
Village: Badmal
Risk Level: Low Risk
Cluster: 2
Top Contaminants:
NO3, Mg, F
Possible Health Risks:
Blue baby syndrome
Methemoglobinemia
Thyroid problems


---

# 🛠 Tech Stack

- Python  
- Scikit-learn  
- Pandas  
- NumPy  
- FastAPI  
- Streamlit  
- Uvicorn  
- Render (API deployment)  
- Streamlit Cloud (UI deployment)  
- GitHub  

---

# 🧬 Machine Learning Methodology

- Feature engineering from groundwater dataset  
- WHO-based contaminant safe limits  
- Weighted health risk scoring  
- Agglomerative clustering for zone detection  
- Risk-level labeling using cluster severity  
- Contaminant ranking using normalized exceedance  
- Disease prediction using weighted mapping  
- Explainable AI-based groundwater intelligence  

---


---

# ⚙️ Installation

Clone repository
git clone https://github.com/yourusername/groundwater-risk.git
cd groundwater-risk

Create virtual environment
python -m venv myenv
source myenv/bin/activate


Install dependencies
pip install -r requirements.txt


---

# ▶️ Run Locally

## Run FastAPI
uvicorn app.api:app --reload


## Run Streamlit
streamlit run streamlit_app.py


---

# 🔌 API Usage

### Request

GET /predict?village=Badmal
### Response

```json
{
  "status": "success",
  "data": {
    "village": "Badmal",
    "risk_level": "Low Risk",
    "cluster": 2,
    "top_contaminants": ["NO3","Mg","F"],
    "possible_diseases": [
      "Blue baby syndrome",
      "Methemoglobinemia",
      "Thyroid problems"
    ]
  }
}

```
---
# 📊 Dataset

Groundwater contamination dataset containing:

- NO3  
- F  
- Cl  
- SO4  
- TH  
- Ca  
- Mg  
- Na  
- Fe  
- Raster value  
- Village name  


---

# 🔮 Future Improvements

- Interactive contamination map  
- Real-time groundwater monitoring  
- Satellite raster integration  
- Deep learning risk prediction  
- Temporal groundwater trend analysis  
- Multi-district scaling  

---

# 👩‍💻 Author

**Prachya Das**  
CSE (AI & ML)  
Cybersecurity & Machine Learning Enthusiast  

---

# ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to contribute!



