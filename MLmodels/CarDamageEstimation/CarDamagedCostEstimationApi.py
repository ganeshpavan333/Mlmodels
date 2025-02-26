import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import joblib
from ultralytics import YOLO
import cv2
from fastapi import FastAPI, UploadFile, File ,Form
from fastapi.responses import JSONResponse
import io
from PIL import Image

app = FastAPI()

# Load the trained cost estimation model and encoders
cost_model = joblib.load("car_damage_cost_model.pkl")
company_encoder = joblib.load("company_encoder.pkl")
part_encoder = joblib.load("part_encoder.pkl")

# Load the trained YOLO model for damaged parts detection
best_model_path = "runs/detect/train4/weights/best.pt"
trained_model = YOLO(best_model_path)

# Cost estimation dataset for validation (optional)
cost_data = pd.read_csv("C:\\Users\\GaneshMunduri\\Desktop\\car_damaged_parts_costs_inr.csv")

# Inverse transform function to get part name from label encoding
def get_part_name(label):
    return part_encoder.inverse_transform([label])[0]

# Function to estimate cost for a detected damaged part
def estimate_part_cost(part_name, company_name):
    # Encode the inputs
    encoded_part = part_encoder.transform([part_name])[0]
    encoded_company = company_encoder.transform([company_name])[0]

    # Predict the cost using the trained model
    input_data = np.array([[encoded_company, encoded_part]])
    estimated_cost = cost_model.predict(input_data)[0]
    return round(estimated_cost, 2)

@app.post("/predict/")
async def predict_damage(company_name: str = Form(...), file: UploadFile = File(...)):
    # Read image from request
    image_data = await file.read()
    image = Image.open(io.BytesIO(image_data))
    image = np.array(image)

    # Run inference on the image
    results = trained_model(image, save=True, conf=0.5)

    # Extract damaged parts and estimate their costs
    damaged_parts_costs = {}

    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])  # Predicted class ID
            class_name = trained_model.names[class_id]  # Class name from YOLO model
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box coordinates
            image_width = image.shape[1]

            # Determine left/right for headlights
            if "headlight" in class_name.lower():
                position = "left" if (x1 + x2) / 2 < image_width / 2 else "right"
                class_name = f"damaged {position} headlight"

            # Determine front/rear for bumpers
            if "bumper" in class_name.lower():
                position = "front" if y1 < image_width / 2 else "rear"
                class_name = f"damaged {position} bumper"

            # Estimate the cost for the detected part
            try:
                part_cost = estimate_part_cost(class_name, company_name)
            except ValueError:
                part_cost = "Cost not available"  # Handle unseen parts gracefully

            damaged_parts_costs[class_name] = part_cost

    return JSONResponse(content={"damaged_parts_with_costs": damaged_parts_costs})

# To run: uvicorn CarDamagedCostEstimationApi:app --reload
