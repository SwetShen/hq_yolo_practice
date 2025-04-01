from ultralytics import YOLO

onnx_model = YOLO("../06-web-serve/save/yolov5su.onnx")

# Run inference
results = onnx_model(["./bus.jpg"], task='detect')
results[0].save()
# print(results.sa)

# 高级操作：获取检测信息
# boxes = results[0].boxes  # 检测框对象
# print(f"检测到 {len(boxes)} 个目标")
# for box in boxes:
#     print(f"类别: {onnx_model.names[box.cls.item()]} 置信度: {box.conf.item():.2f}")
