import torch
import torch.nn as nn
import torch.nn.functional as F

class GoogLeNet(nn.Module):
    def __init__(self, n_classes):
        super(GoogLeNet, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=10, kernel_size=7, stride=2)
        self.pool1 = nn.MaxPool2d(kernel_size=3, stride=2)
        self.local_response_norm = nn.LocalResponseNorm(10)
        self.conv2 = nn.Conv2d(in_channels=10, out_channels=32, kernel_size=1)
        self.conv3 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, padding=1)
        self.local_response_norm1 = nn.LocalResponseNorm(64)
        self.pool2 = nn.MaxPool2d(kernel_size=3, stride=2)

    def forward(self, x):
        x = self.conv1(x)
        x = self.pool1(x)
        x = self.local_response_norm(x)
        x = self.conv2(x)
        x = self.conv3(x)
        x = self.local_response_norm1(x)
        x = self.pool2(x)
        return F.relu(x)
