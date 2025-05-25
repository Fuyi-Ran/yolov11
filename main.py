import torch, thop
from thop import profile
import torch.nn as nn
import torch.nn.functional as F

if __name__ == '__main__':
    input1 = torch.randn((1, 128, 32, 32))
    
    linear_layer = nn.Linear(128, 64, bias=False)
    linear_output = linear_layer(input1.permute((0, 2, 3, 1))).permute((0, 3, 1, 2))
    
    conv_output = F.conv2d(input1, linear_layer.weight[:, :, None, None], bias=linear_layer.bias)
    # conv_output = F.conv2d(input1, linear_layer.weight[:, :, None, None])
    print(torch.sqrt((conv_output - linear_output) ** 2).sum())