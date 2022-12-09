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
        self.inception1 = InceptionBlock(64)

    def forward(self, x):
        x = self.conv1(x)
        x = self.pool1(x)
        x = self.local_response_norm(x)
        x = self.conv2(x)
        x = self.conv3(x)
        x = self.local_response_norm1(x)
        x = self.pool2(x)
        x = self.inception1(x)
        return F.relu(x)






class InceptionBlock(nn.Module):
    def __init__(self, in_channels):
        super(InceptionBlock, self).__init__()
        conv = Block
        self.conv1_11 = conv(in_channels=in_channels, out_channels=in_channels+10, kernel=1)
        self.conv1_12 = conv(in_channels=in_channels, out_channels=in_channels+10, kernel=1)
        self.pool1_1 = conv(in_channels=in_channels, out_channels=in_channels+10, kernel=3, padding=1)
        self.conv2_11 = conv(in_channels=in_channels, out_channels=in_channels+20, kernel=1)
        self.conv2_31 = conv(in_channels=in_channels+10, out_channels=in_channels+20, kernel=3, padding=1)
        self.conv2_51 = conv(in_channels=in_channels+10, out_channels=in_channels+20, kernel=5, padding=2)
        self.conv2_12 = conv(in_channels=in_channels+10, out_channels=in_channels+20, kernel=1)

    def forward(self, x):
        first = self.conv2_11(x)
        second = self.conv1_11(x)
        second = self.conv2_31(second)
        third = self.conv1_12(x)
        third = self.conv2_51(third)
        end = F.max_pool2d(self.pool1_1(x), kernel_size=3, padding=1)
        print(end.shape)
        end = self.conv2_12(end)
        res = [first, second, third, end]
        for i in res:
            print(i.shape)
        return torch.cat(res, 1)



class Block(nn.Module):
    def __init__(self, in_channels, out_channels, kernel, stride=1, padding=0):
        super(Block, self).__init__()
        self.conv = nn.Conv2d(in_channels=in_channels, out_channels=out_channels, kernel_size=kernel, stride=stride, padding=padding)
        self.batch = nn.BatchNorm2d(out_channels)

    def forward(self, x):
        x = self.conv(x)
        x = self.batch(x)
        return F.relu(x, inplace=True)
