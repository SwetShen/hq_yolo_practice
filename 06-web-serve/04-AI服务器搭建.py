from flask import Flask
from flask import render_template
from flask import request
import torch
import cv2
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ========================加载模型结构=============================
from torch import nn

model = nn.Sequential(
    nn.Conv2d(3, 16, 3, 1, 1),  # （16 x 28 x 28）
    nn.ReLU(),  # 激活函数
    nn.MaxPool2d(2, 2),  # （16 x 14 x 14）
    nn.Conv2d(16, 32, 3, 1, 1),  # （32 x 14 x 14）
    nn.ReLU(),  # 激活函数
    nn.MaxPool2d(2, 2),  # （32 x 7 x 7） # 最后一个卷积的图像大小（5，6，7，8）
    nn.Flatten(),  # 展平特征到（1568）
    nn.Linear(32 * 7 * 7, 1024),
    nn.ReLU(),  # 激活函数
    nn.Linear(1024, 10),  # 最终输出为分类的数量
    nn.LogSoftmax(dim=-1)  # softmax 激活函数
)
# ===========================加载权重 ==========================
state_dict = torch.load("./static/save/best.pt", weights_only=True)
model.load_state_dict(state_dict)  # 模型结构加入权重


# ---- 渲染整个识别的网页-----
@app.route("/")
def detect_number():
    return render_template("index.html")


# ---- 上传文件，并识别该内容 ----
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']  # 获取文件对象
        f.save('./static/upload/uploaded_file.png')  # 将文件对象保存到服务器
        # ---- 识别本地文件--------
        img = cv2.imread("./static/upload/uploaded_file.png")
        # img = cv2.resize(img,(28,28))
        img = np.expand_dims(img, 0)
        img = torch.from_numpy(img)
        img = torch.permute(img, [0, 3, 1, 2])
        model_cpu = model.to(torch.device("cpu"))
        predict = model_cpu(img.float())
        result = torch.argmax(predict, dim=-1)

    return {"code": 202, "result": result[0].item()}


if __name__ == "__main__":
    app.run("0.0.0.0", 9000, debug=True)
