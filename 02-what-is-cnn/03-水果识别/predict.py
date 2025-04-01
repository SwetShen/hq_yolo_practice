import torch
from torch import nn
from torchvision import transforms
from PIL import Image
import cv2

# ========================加载模型结构=============================
device = torch.device("cuda")

model = nn.Sequential(
    nn.Conv2d(3, 16, 3, 1, 1),
    nn.ReLU(),
    nn.MaxPool2d(2, 2),
    nn.Conv2d(16, 32, 3, 1, 1),
    nn.ReLU(),
    nn.MaxPool2d(2, 2),
    nn.Conv2d(32, 64, 3, 1, 1),
    nn.ReLU(),
    nn.MaxPool2d(2, 2),
    nn.Conv2d(64, 128, 3, 1, 1),
    nn.ReLU(),
    nn.MaxPool2d(2, 2),
    nn.Flatten(),
    nn.Dropout(),
    nn.Linear(6 * 6 * 128, 1024),
    nn.ReLU(),
    nn.Linear(1024, 3),
    nn.LogSoftmax(dim=-1)
)

model.load_state_dict(torch.load("./save/best1.pt"))
model = model.to(device)
model.eval()

# ========================数据预处理=============================
# 使用与训练相同的预处理（去除数据增强）
test_transform = transforms.Compose([
    transforms.Resize(100),
    transforms.CenterCrop(100),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# ========================加载并处理图像=============================
image = cv2.imread("./data/fruits/Watermelon/0_100.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # BGR转RGB
pil_image = Image.fromarray(image)  # 转换为PIL图像

# 应用预处理
input_tensor = test_transform(pil_image).unsqueeze(0).to(device)  # 添加batch维度并移至GPU

# ========================预测=============================
with torch.no_grad():
    output = model(input_tensor.float())
pred = torch.argmax(output, dim=-1)
print("预测结果：", pred.item())