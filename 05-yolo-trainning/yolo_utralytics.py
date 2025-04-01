from ultralytics import YOLO
import collections

# Load a model
model = YOLO("./data/yolov5su.pt")  # pretrained YOLO11n model

# Run batched inference on a list of images
results = model(["./bus.jpg"])  # return a list of Results objects

# Process results list
for result in results:
    print(result.names)
    boxes = result.boxes  # Boxes object for bounding box outputs
    data_list = [result.names[i.item()] for i in boxes.data[:, -1]]
    print("out", dict(collections.Counter(data_list)))
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs
    obb = result.obb  # Oriented boxes object for OBB outputs
    # result.show()  # display to screen
    # result.save(filename="result.jpg")  # save to disk
