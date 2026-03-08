# Hypertension Stage Prediction System

This project is a Machine Learning based web application that predicts the stage of hypertension based on patient demographic and clinical parameters.

The system analyzes patient health information such as blood pressure ranges, age group, medical history, and symptoms to determine the hypertension stage.

---

## Project Overview

Hypertension (high blood pressure) is a major health condition that can lead to severe complications if not detected early.  
This project builds a machine learning model that predicts the hypertension stage using patient data.

The system includes:

- Data preprocessing
- Exploratory Data Analysis (EDA)
- Machine learning model training and comparison
- Model persistence
- Prediction module
- Flask web application for user interaction

---

## Dataset Features

The dataset contains patient information including:

- Gender
- Age Group
- Medical History
- Medication Status
- Symptoms (Breath Shortness, Visual Changes, Nose Bleeding)
- Blood Pressure (Systolic & Diastolic)
- Controlled Diet

Target variable:

- **Hypertension Stage**

Example stages:

- NORMAL
- HYPERTENSION (Stage-1)
- HYPERTENSION (Stage-2)
- HYPERTENSIVE CRISIS

---

## Machine Learning Models Used

The following models were trained and compared:

- Logistic Regression
- Decision Tree
- Random Forest
- Support Vector Machine (SVM)

The best performing model was selected and saved for deployment.

---

## Project Structure
