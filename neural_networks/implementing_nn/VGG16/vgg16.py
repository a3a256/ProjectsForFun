import torch.nn as nn
import torch.nn.functional as F
import torch


class VGG16(nn.Module):
    def __init__(self):
        super(VGG16, self).__init__()
        self.layers = nn.Sequential(
            Branch1(),
            nn.MaxPool2d(kernel_size=2, stride=2),
            Branch2(),
            nn.MaxPool2d(kernel_size=2, stride=2),
            Branch3(),
            nn.MaxPool2d(kernel_size=2, stride=2),
            Branch4(256, 512),
            nn.MaxPool2d(kernel_size=2, stride=2),
            Branch4(512, 512),
            nn.MaxPool2d(kernel_size=2, stride=2),
        )
        self.fc = nn.Sequential(
            nn.Linear(1024, 4096),
            nn.Linear(4096, 4096),
            nn.Linear(4096, 1000)
        )

    def forward(self, x):
        x = self.layers(x)
        x = torch.flatten(x)
        x = self.fc(x)
        return F.softmax(x, dim=0)


class Branch1(nn.Module):
    def __init__(self):
        super(Branch1, self).__init__()
        block = CNNBlock
        self.branch = nn.Sequential(block(3, 64, 3), block(64, 64, 3))
    
    def forward(self, x):
        return F.relu(self.branch(x), inplace=True)


class Branch2(nn.Module):
    def __init__(self):
        super(Branch2, self).__init__()
        block = CNNBlock
        self.branch = nn.Sequential(block(64, 128, 3), block(128, 128, 3))
    
    def forward(self, x):
        return F.relu(self.branch(x), inplace=True)


class Branch3(nn.Module):
    def __init__(self):
        super(Branch3, self).__init__()
        block = CNNBlock
        self.branch = nn.Sequential(block(128, 256, 3), block(256, 256, 3), block(256, 256, 3))
    
    def forward(self, x):
        return F.relu(self.branch(x), inplace=True)


class Branch4(nn.Module):
    def __init__(self, in_channels, out_channels):
        super(Branch4, self).__init__()
        block = CNNBlock
        self.branch = nn.Sequential(block(in_channels, out_channels, 3), block(out_channels, out_channels, 3), block(out_channels, out_channels, 3))
    
    def forward(self, x):
        return F.relu(self.branch(x), inplace=True)


class CNNBlock(nn.Module):
    def __init__(self, in_channels, out_channels, kernel, padding=0, stride=1):
        super(CNNBlock, self).__init__()
        self.layer = nn.Conv2d(in_channels=in_channels, out_channels=out_channels, kernel_size=kernel, padding=padding, stride=stride)
        self.batch = nn.BatchNorm2d(out_channels)

    def forward(self, x):
        return F.relu(self.batch(self.layer(x)), inplace=True)