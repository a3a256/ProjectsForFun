import torch.nn as nn
import numpy as np
import torch
import torchvision
import torch.nn.functional as F
import os
import time

class Inception(nn.Module):
    def __init__(self, n_classes):
        super(Inception, self).__init__()
        conv = Block
        self.conv1 = conv(3, 10, 1)
        self.conv2 = conv(3, 10, 3, 1)
        self.conv3 = conv(3, 10, 5, 2)
        self.pool = conv(3, 10, 3, 1)
        self.linear = nn.Linear(720, 1024)
        self.fc = torch.nn.Linear(1024, n_classes)

    def forward(self, x):
        a = self.conv1(x)
        # a = a.view(a.shape[0], )
        b = self.conv2(x)
        # b = b.view(b.shape[0], b.shape[1], 224, 224)
        c = self.conv3(x)
        # c = c.view(b.shape[0], -1)
        po = F.avg_pool2d(x, kernel_size=3, stride=1, padding=1)
        d = self.pool(po)
        # d = d.view(d.shape[0], -1)
        out = [a, b, c, d]
        # print(a.shape)
        # print(b.shape)
        # print(c.shape)
        # print(d.shape)
        res = torch.cat(out, 1)
        max_pool = nn.AdaptiveMaxPool2d(720)
        change = max_pool(res)
        return self.fc(self.linear(change))



class Block(nn.Module):
    def __init__(self, in_channels, out_channels, kernel, padding=0):
        super(Block, self).__init__()
        self.conv2d = torch.nn.Conv2d(in_channels=in_channels, out_channels=out_channels, kernel_size=(kernel, kernel), padding=padding)
        self.batch = torch.nn.BatchNorm2d(out_channels)

    def forward(self, x):
        x = self.conv2d(x)
        return F.relu(self.batch(x), inplace=True)