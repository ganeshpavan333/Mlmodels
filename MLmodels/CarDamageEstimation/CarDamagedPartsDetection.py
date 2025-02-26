from ultralytics import YOLO
import torch
import cv2
import os

# Step 1: Load Pre-trained YOLOv8 Model
model = YOLO("yolov8n.pt")  # You can change to 'yolov8s.pt', 'yolov8m.pt' for better accuracy

# Step 2: Train the Model
model.train(
    data="config.yaml",  # Config file with correct dataset paths
    epochs=50,
    imgsz=640,
    batch=16,
    workers=4,
    device="cuda" if torch.cuda.is_available() else "cpu"
)

# Step 3: Save the Best Model in PyTorch Format
