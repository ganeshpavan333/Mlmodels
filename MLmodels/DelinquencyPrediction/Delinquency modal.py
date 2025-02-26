import pandas as pd 
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load the dataset
data_path = "C:\\Users\\GaneshMunduri\\Desktop\\large_delinquency_data.csv"  # Update the path if needed
df = pd.read_csv(data_path)

# Display first few rows
print("Dataset Preview:")
print(df.head())

# Encode categorical variables
label_encoders = {}
categorical_columns = ["Marital_Status", "Employment_Status", "Loan_Purpose"]
for col in categorical_columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Define features and target variable
X = df.drop(columns=["Borrower_ID", "Delinquent"])  # Exclude ID and target column
y = df["Delinquent"]

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize numerical features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train a Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model, scaler, and label encoders
joblib.dump(model, "delinquency_model.pkl")
joblib.dump(scaler, "scaler.pkl")
joblib.dump(label_encoders, "label_encoders.pkl")

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")
print("Classification Report:")
print(classification_report(y_test, y_pred))

def transform_input(input_data, label_encoders, scaler):
    transformed_input = []
    
    # Iterate over each categorical column and transform using the respective label encoder
    for col in input_data:
        if col in label_encoders:
            le = label_encoders[col]
            transformed_input.append(le.transform([input_data[col]])[0])  # Apply transformation and append
        else:
            transformed_input.append(input_data[col])  # For non-categorical columns, just append
        
    
    # Scale numerical features
    transformed_input = np.array(transformed_input).reshape(1, -1)  # Reshape for prediction
    transformed_input_scaled = scaler.transform(transformed_input)  # Scale input
    
    return transformed_input_scaled

# Example: Predict delinquency for a new borrower

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
print(transform_input)
#new_borrower = np.array([[30, 1, 0, 40000, 35, 580, 14000, 36, 10, 2, 40, 3, 9]])  
new_borrower = np.array([[34, 2, 1, 77199, 34.25, 823, 12578, 48, 18.49, 0, 2, 13.55, 3]]) 


new_borrower = scaler.transform(new_borrower)  # Scale input

# Predict delinquency
prediction = model.predict(transformed_input)
print("Predicted Delinquency:", "Yes" if prediction[0] == 1 else "No")

probabilities = model.predict_proba(transformed_input)

# Get the probability of delinquency (class 1)
delinquency_probability = probabilities[0][1]  # Probability of class 1 (delinquent)
print(f"Percentage of Delinquency: {delinquency_probability * 100:.2f}%")
