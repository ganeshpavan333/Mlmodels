Machine Learning Models Repository

This repository contains two machine learning models:

Delinquency Prediction Model – Predicts the likelihood of a customer defaulting on a loan.
Car Damage Detection & Cost Estimation Model – Identifies damaged car parts from images and estimates the repair cost.

📌 Models Overview

1️⃣ Delinquency Prediction Model

Objective: Predict customer delinquency based on historical financial data.

Approach:

Data preprocessing (handling missing values, encoding categorical variables).

Feature engineering and selection.

Model training using Random Forest.

Model evaluation using metrics like Accuracy, Precision, Recall, and AUC-ROC.

Tech Stack: Python, Pandas, NumPy, Scikit-learn, joblib, pydantic, FastApi (for API deployment).


2️⃣ Car Damage Detection & Cost Estimation Model

Objective: Identify damaged parts in car images and estimate the repair cost.

Approach:

YOLO-based Object Detection to identify damaged parts.

Bounding Box Classification for damage severity (minor, moderate, severe).

Regression Model for cost estimation based on detected damages and car details.

Tech Stack: Python, ultralytics, Pandas, NumPy, Scikit-learn, joblib, pydantic, FastApi (for API deployment).
