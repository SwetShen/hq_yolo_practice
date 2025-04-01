from ultralytics import YOLO

"""
pip install onnx onnxslim onnxruntime
"""

# Load a model
model = YOLO("./data/yolov5s.pt")  # load a custom trained model

# Export the model
# model.export(format="onnx")

model.export(format="tfjs")