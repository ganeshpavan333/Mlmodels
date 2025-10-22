from typing import List
import numpy as np
import joblib
import io
from PIL import Image
from ultralytics import YOLO
from fastapi import FastAPI, UploadFile, File, Form, Header, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from esgdata import ESG_Data

# Initialize FastAPI
app = FastAPI(title="Car Damage & Delinquency Prediction API", version="1.0")

# API Key Setup
API_KEY = "your Api Key here"

# Load Delinquency Prediction Model and Encoders
model = joblib.load("delinquency_model.pkl")
scaler = joblib.load("scaler.pkl")
label_encoders = joblib.load("label_encoders.pkl")

# Load Car Damage Prediction Model and Encoders
cost_model = joblib.load("car_damage_cost_model.pkl")
company_encoder = joblib.load("company_encoder.pkl")
part_encoder = joblib.load("part_encoder.pkl")
trained_model = YOLO("runs/detect/train4/weights/best.pt")

# Customer Details Schema
class CustomerDetails(BaseModel):
    Name: str
    Id: str
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

# Transform function for loan data
def transform_input(input_data: dict):
    transformed_input = []

    for col in input_data:
        if col =="Name" or col =="Id":
            continue

        if col in label_encoders:
            le = label_encoders[col]
            transformed_input.append(le.transform([input_data[col]])[0])
        
        else:
            transformed_input.append(input_data[col])

    transformed_input = np.array(transformed_input).reshape(1, -1)

    return scaler.transform(transformed_input)

@app.post("/delinquency")
def predict_delinquency(data: List[CustomerDetails], x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")
    
    try:
        predictions = []

        for application in data:
            input_dict = application.dict()
            Name_Given , Id_Given = input_dict["Name"],input_dict["Id"]
            transformed_input = transform_input(input_dict)

            # Predict delinquency
            prediction = model.predict(transformed_input)[0]
            probabilities = model.predict_proba(transformed_input)[0][1] * 100  # Probability of delinquency

            predictions.append({
                "Name" : Name_Given,
                "Id":Id_Given,
                "delinquency": "Yes" if prediction == 1 else "No",
                "Percantage": round(probabilities, 2)
            })

        return {"predictions": predictions}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/CarDamage")
async def predict_damage(company_name: str = Form(...), file: UploadFile = File(...), x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")
    
    image_data = await file.read()
    image = Image.open(io.BytesIO(image_data))
    image = np.array(image)
    results = trained_model(image, save=False, conf=0.5)
    damaged_parts_costs = {}

    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])
            class_name = trained_model.names[class_id]
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            image_width = image.shape[1]

            if "headlight" in class_name.lower():
                position = "left" if (x1 + x2) / 2 < image_width / 2 else "right"
                class_name = f"damaged {position} headlight"

            if "bumper" in class_name.lower():
                position = "front" if y1 < image_width / 2 else "rear"
                class_name = f"damaged {position} bumper"
            
            try:
                encoded_part = part_encoder.transform([class_name])[0]
                encoded_company = company_encoder.transform([company_name])[0]
                input_data = np.array([[encoded_company, encoded_part]])
                part_cost = round(cost_model.predict(input_data)[0], 2)

            except ValueError:
                part_cost = "Cost not available"
            damaged_parts_costs[class_name] = part_cost

    return JSONResponse(content={"damaged_parts_with_costs": damaged_parts_costs})

class ESGResponse(BaseModel):
    CompanyName: str
    Industry: str
    Revenue: str
    EnvironmentData: dict
    SocialData: dict
    GovernanceData: dict


@app.get("/companyesg", response_model=ESGResponse)
def get_esg_data(company_name: str = Query(...), industry: str = Query(...), x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")
    
    key = (company_name.lower(), industry.lower())
    if key in ESG_Data:
        return ESG_Data[key]
    raise HTTPException(status_code=404, detail="Company with specified industry not found")



@app.get("/")
def home(x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")
    
    return {"message": "Car Damage & Delinquency Prediction API is running!"}
