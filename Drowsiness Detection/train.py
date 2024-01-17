from PIL import Image
import matplotlib.pyplot as plt
import ultralytics
from ultralytics import YOLO

ultralytics.checks()

yolo8_model = YOLO('yolov8x.yaml').load('yolov8x.pt')


# def freeze_layer(trainer):
#     model = trainer.model
#     num_freeze = 10
#     print(f"Freezing {num_freeze} layers")
#     freeze = [f'model.{x}.' for x in range(num_freeze)]  # layers to freeze
#     for k, v in model.named_parameters():
#         v.requires_grad = True  # train all layers
#         if any(x in k for x in freeze):
#             print(f'freezing {k}')
#             v.requires_grad = False
#     print(f"{num_freeze} layers are frozen.")
#
#
# # Logging
# log = yolo8_model.add_callback("on_train_start", freeze_layer)

# Training
yolo8_model.train(
    data="./data/custom_data.yaml",
    epochs=25,
    batch=16,
    imgsz=640,
    conf=0.25
)

# Save model Weights
yolo8_model.export(
    model="/runs/detect/train4/weights/best.pt",
    format="onnx"
)

# Validation
yolo8_model.val(
    model="runs/detect/train4/weights/best.onnx",
    imgsz=640,
    data="./data/custom_data.yaml"
)

# Prediction
yolo8_model.predict(
    model="runs/detect/train4/weights/best.onnx",
    imgsz=640,
    source=["./data/test/images/SGA2101132S0125IMG0005_jpg.rf.bfbeefa7a5f04a2ee3999623d54b035b.jpg",
            "./data/test/images/SGA2101132S0140IMG0001_jpg.rf.4325bd399fb5cddc590f731e9a0a5ddf.jpg",
            "./data/test/images/SGA2101132S0151IMG0002_jpg.rf.b1d67a0eef9b32dedba446ff99e5b5db.jpg"]
)

# Path to the predicted image
predicted_image_path = "./data/test/images/SGA2101132S0125IMG0005_jpg.rf.bfbeefa7a5f04a2ee3999623d54b035b.jpg"

# Load the predicted image
predicted_image = Image.open(predicted_image_path)

# Display the predicted image using matplotlib
plt.imshow(predicted_image)
plt.axis('off')
plt.show()

# Path to the predicted image
predicted_image_path = "./data/test/images/SGA2101132S0140IMG0001_jpg.rf.4325bd399fb5cddc590f731e9a0a5ddf.jpg"

# Load the predicted image
predicted_image = Image.open(predicted_image_path)

# Display the predicted image using matplotlib
plt.imshow(predicted_image)
plt.axis('off')
plt.show()

# Path to the predicted image
predicted_image_path = "./data/test/images/SGA2101132S0151IMG0002_jpg.rf.b1d67a0eef9b32dedba446ff99e5b5db.jpg"

# Load the predicted image
predicted_image = Image.open(predicted_image_path)

# Display the predicted image using matplotlib
plt.imshow(predicted_image)
plt.axis('off')
plt.show()