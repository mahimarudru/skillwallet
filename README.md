# Hypertension Stage Prediction System

This project is a **Machine Learning-based web application** that predicts the stage of hypertension based on patient demographic and clinical parameters.

The system analyzes patient health information such as blood pressure ranges, age group, medical history, and symptoms to determine the hypertension stage.

---

# Project Overview

Hypertension (high blood pressure) is a major health condition that can lead to severe complications if not detected early.

This project builds a **machine learning model** that predicts the hypertension stage using patient data.

The system includes:

- Data preprocessing
- Exploratory Data Analysis (EDA)
- Machine learning model training and comparison
- Model persistence
- Prediction module
- Flask web application for user interaction

---

# Dataset Features

The dataset contains patient information including:

- Gender
- Age Group
- Medical History
- Medication Status
- Symptoms
  - Breath Shortness
  - Visual Changes
  - Nose Bleeding

- Blood Pressure
  - Systolic
  - Diastolic

- Controlled Diet

### Target Variable

**Hypertension Stage**

Example stages:

- NORMAL
- HYPERTENSION (Stage-1)
- HYPERTENSION (Stage-2)
- HYPERTENSIVE CRISIS

---

# Machine Learning Models Used

The following models were trained and compared:

- Logistic Regression
- Decision Tree
- Random Forest
- Support Vector Machine (SVM)

The best-performing model was selected and saved for deployment.

---

# Project Structure

```
skillwallet
│
├── app
│   ├── static
│   ├── templates
│   │   └── index.html
│   └── app.py
│
├── data
│   └── patient_data.csv
│
├── model
│   ├── anemia_model.pkl
│   └── scaler.pkl
│
├── notebooks
│   └── EDA.ipynb
│
├── src
│   ├── preprocessing.py
│   ├── train_model.py
│   └── predict.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Workflow

```
User Input (Web Form)
        ↓
Flask Web Application
        ↓
Prediction Module
        ↓
Feature Preprocessing
        ↓
Machine Learning Model
        ↓
Predicted Hypertension Stage
```

---

# Exploratory Data Analysis

EDA was performed to understand the dataset before model training.

Key analysis included:

- Dataset overview
- Missing value detection
- Stage distribution
- Age group distribution
- Blood pressure vs stage relationship
- Feature correlation analysis

EDA notebook:

```
notebooks/EDA.ipynb
```

---

# Installation

### Clone the repository

```
git clone https://github.com/mahimarudru/skillwallet.git
cd skillwallet
```

### Create virtual environment

```
python -m venv .venv
```

### Activate environment

**Windows**

```
.venv\Scripts\activate
```

**Linux / Mac**

```
source .venv/bin/activate
```

### Install dependencies

```
pip install -r requirements.txt
```

---

# Running the Application

Start the Flask server:

```
python app/app.py
```

Open your browser and go to:

```
http://127.0.0.1:5000
```

Enter patient details and the system will predict the hypertension stage.

---

# Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Flask
- Joblib
- Jupyter Notebook

---

# Future Improvements

- Improve UI using Bootstrap or Tailwind
- Add model explainability (SHAP or feature importance)
- Deploy the application online (Render / AWS / Heroku)
- Use real clinical datasets for better model generalization

---

# Author

Mahima Rudru
B.Tech Artificial Intelligence and Data Science
Amrita Vishwa Vidyapeetham

---

# GitHub Repository

```
https://github.com/mahimarudru/skillwallet
```
