import torch
import torch.onnx

input_shape = (1,3,224,224)
dummpy_input = torch.randn(input_shape)

