import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib

# Load the updated dataset
csv_path = "C:\\Users\\GaneshMunduri\\Desktop\\car_damaged_parts_costs_inr.csv"  # Replace with your path
df = pd.read_csv(csv_path)

# Encode categorical features
le_company = LabelEncoder()
df['company'] = le_company.fit_transform(df['company'])

le_part = LabelEncoder()
df['part_name'] = le_part.fit_transform(df['part_name'])

# Features and target
X = df[['company', 'part_name']]
y = (df['min_cost_inr'] + df['max_cost_inr']) / 2  # Average cost as the target

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Hyperparameter tuning
param_dist = {
    'n_estimators': [100, 200, 300, 500],
    'max_depth': [10, 20, 30, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': ['auto', 'sqrt', 'log2']
}

rf = RandomForestRegressor(random_state=42)

# Randomized search
random_search = RandomizedSearchCV(estimator=rf, param_distributions=param_dist, n_iter=50, cv=5, n_jobs=-1, verbose=2, random_state=42)
random_search.fit(X_train, y_train)

# Best model from hyperparameter tuning
best_model = random_search.best_estimator_

# Predictions
y_pred = best_model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Absolute Error: {mae}")
print(f"Mean Squared Error: {mse}")
print(f"R2 Score: {r2}")

# Save the model and encoders
joblib.dump(best_model, "car_damage_cost_model.pkl")
joblib.dump(le_company, "company_encoder.pkl")
joblib.dump(le_part, "part_encoder.pkl")

print("✅ Model and encoders saved with hyperparameter tuning!")

# Usage example (to predict cost for a given company and part)
# loaded_model = joblib.load("car_damage_cost_model.pkl")
# company_encoded = le_company.transform(["Toyota"])[0]
# part_encoded = le_part.transform(["damaged door"])[0]
# predicted_cost = loaded_model.predict([[company_encoded, part_encoded]])[0]
# print(f"Estimated Repair Cost: ₹{predicted_cost}")
