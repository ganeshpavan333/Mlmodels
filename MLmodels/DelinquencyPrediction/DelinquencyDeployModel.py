from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import joblib

# Load the saved model, scaler, and label encoders
model = joblib.load("delinquency_model.pkl")
scaler = joblib.load("scaler.pkl")
label_encoders = joblib.load("label_encoders.pkl")

# Initialize FastAPI app
app = FastAPI(title="Delinquency Prediction API", version="1.0")

class LoanApplication(BaseModel):
    Age: int
    Marital_Status: str
    Employment_Status: str
    Annual_Income: float
    Debt_to_Income_Ratio: float
    Credit_Score: int
    Loan_Amount: float
    Loan_Term_Months: int
    Interest_Rate: float
    Loan_Purpose: str
    Missed_Payments_Last_12M: int
    Credit_Utilization_Ratio: float
    Overdraft_Frequency: int

def transform_input(input_data: dict):
    """Convert categorical values to numerical and scale input features."""
    transformed_input = []
    for col in input_data:
        if col in label_encoders:
            le = label_encoders[col]
            transformed_input.append(le.transform([input_data[col]])[0])
        else:
            transformed_input.append(input_data[col])
    
    transformed_input = np.array(transformed_input).reshape(1, -1)
    transformed_input_scaled = scaler.transform(transformed_input)
    
    return transformed_input_scaled

@app.post("/predict")
def predict(data: LoanApplication):
    """Predicts delinquency based on input data."""
    try:
        input_dict = data.dict()
        transformed_input = transform_input(input_dict)

        # Predict delinquency
        prediction = model.predict(transformed_input)[0]
        probabilities = model.predict_proba(transformed_input)[0][1] * 100  # Probability of delinquency

        return {
            "delinquency": "Yes" if prediction == 1 else "No",
            "probability": round(probabilities, 2)
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/")
def home():
    """Basic API status check."""
    return {"message": "Delinquency Prediction API is running!"}
