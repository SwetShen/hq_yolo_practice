from flask import Flask
from flask import request, render_template
from flask_cors import CORS
from datetime import datetime
import os
from ultralytics import YOLO
import collections

app = Flask(__name__)
CORS(app)
onnx_model = YOLO("./save/yolov5su.onnx")


@app.route("/")
def hello_world():
    return render_template("upload_test.html")


@app.route("/detect", methods=['POST'])
def upload_file():
    new_file_name = ""
    total_list = []
    if request.method == 'POST':
        f = request.files['file']
        if f is None:
            return {'status': False, 'result': 'unknown'}
        new_file_name = datetime.now().strftime("%Y%m%d%H%M%S")
        path = f'./static/assets/upload_{new_file_name}.jpg'
        f.save(path)
        if os.path.exists(path):
            # Run inference
            results = onnx_model([path], task='detect')
            name_dict = results[0].names
            boxes = results[0].boxes
            total_list = [name_dict[i.item()] for i in boxes.data[:, -1]]

            results[0].save(filename=f"./static/assets/result_{new_file_name}.jpg")
    return {'status': True, 'result': f"/static/assets/result_{new_file_name}.jpg",
            'data': dict(collections.Counter(total_list))}


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9000, debug=True)
