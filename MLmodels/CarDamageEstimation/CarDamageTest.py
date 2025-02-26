from ultralytics import YOLO
import cv2
import os

best_model_path = "runs/detect/train4/weights/best.pt"
print(f"✅ Model trained and saved at: {best_model_path}")

# Step 4: Load the Trained Model for Testing
trained_model = YOLO(best_model_path)

# Step 5: Test the Model on a Sample Image
image_path = "1.jpeg"  # Replace with a real test image
results = trained_model(image_path, save=True, conf=0.5)

# Step 6: Extract Predictions
damaged_parts = {}

for result in results:
    for box in result.boxes:
        class_id = int(box.cls[0])  # Predicted class
        class_name = trained_model.names[class_id]  # Get class name from model
        x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box coordinates
        image_width = cv2.imread(image_path).shape[1]  # Get image width

        # Determine left/right for headlights
        if "headlight" in class_name.lower():
            position = "left" if (x1 + x2) / 2 < image_width / 2 else "right"
            class_name = f"{position} {class_name}"

        # Determine front/rear for bumpers
        if "bumper" in class_name.lower():
            position = "front" if y1 < image_width / 2 else "rear"
            class_name = f"{position} {class_name}"

        if class_name not in damaged_parts:
            damaged_parts[class_name] = 0

        damaged_parts[class_name] += 1

print("Detected damaged parts:")
print(damaged_parts)
