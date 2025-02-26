import numpy as np
import joblib

# Load the saved model, scaler, and label encoders
model = joblib.load("delinquency_model.pkl")
scaler = joblib.load("scaler.pkl")
label_encoders = joblib.load("label_encoders.pkl")

def transform_input(input_data, label_encoders, scaler):
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

# Example input
new_input = {
    "Age": 27,
    "Marital_Status": "Single",
    "Employment_Status": "Unemployed",
    "Annual_Income": 86237,
    "Debt_to_Income_Ratio": 34.08,
    "Credit_Score": 503,
    "Loan_Amount": 47590,
    "Loan_Term_Months": 60,
    "Interest_Rate": 11.29,
    "Loan_Purpose": "Education",
    "Missed_Payments_Last_12M": 4,
    "Credit_Utilization_Ratio": 32.26,
    "Overdraft_Frequency": 0
}



transformed_input = transform_input(new_input, label_encoders, scaler)

# Predict delinquency
prediction = model.predict(transformed_input)
print("Predicted Delinquency For Input1:", "Yes" if prediction[0] == 1 else "No")

probabilities = model.predict_proba(transformed_input)
delinquency_probability = probabilities[0][1]  # Probability of delinquency
print(f"Percentage of Delinquency For Input1: {delinquency_probability * 100:.2f}%")


