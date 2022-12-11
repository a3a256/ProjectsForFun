import torch
import torch.nn as nn
import torch.nn.functional as F

class GoogLeNet(nn.Module):
    def __init__(self, n_classes):
        super(GoogLeNet, self).__init__()
        conv = Block
        self.conv1 = conv(in_channels=3, out_channels=8, kernel=7, stride=2)
        self.pool1 = conv(in_channels=8, out_channels= 16, kernel=3, stride=2)
        self.local_response_norm = nn.LocalResponseNorm(16)
        self.conv2 = conv(in_channels=16, out_channels=8, kernel=1)
        self.conv3 = conv(in_channels=8, out_channels=16, kernel=3, padding=1)
        self.local_response_norm1 = conv(16, 12, kernel=3, padding=1)
        self.pool2 = conv(12, 24, kernel=3, padding=1)
        self.inception1 = InceptionBlock(24, 32, 48)
        self.inception2 = InceptionBlock(192, 128, 96)
        self.inception3 = InceptionBlock(384, 192, 128)
        self.inception4 = InceptionBlock(512, 192, 64)
        self.auxiliary1 = AuxiliaryClassifier(512, 192)
        self.inception5 = InceptionBlock(256, 128, 32)
        self.inception6 = InceptionBlock(128, 64, 32)
        self.inception7 = InceptionBlock(128, 64, 32)
        self.auxiliary2 = AuxiliaryClassifier(128, 64)
        self.inception8 = InceptionBlock(128, 64, 32)
        self.inception9 = InceptionBlock(128, 64, 32)
        self.pool3 = conv(128, 64, 7, 1, 3)
        self.linear = nn.Linear(720, 1)

    def forward(self, x):
        x = self.conv1(x)
        x = F.avg_pool2d(self.pool1(x), kernel_size=3, stride=1, padding=1)
        x = self.local_response_norm(x)
        x = self.conv2(x)
        x = self.conv3(x)
        x = F.local_response_norm(self.local_response_norm1(x), 12)
        x = F.max_pool2d(self.pool2(x), kernel_size=3, stride=1, padding=1)
        x = self.inception1(x)
        x =self.inception2(x)
        x = self.inception3(x)
        softmax0 = self.auxiliary1(x)
        x = self.inception4(x)
        x = self.inception5(x)
        x = self.inception6(x)
        softmax1 = self.auxiliary2(x)
        x = self.inception7(x)
        x = self.inception8(x)
        x = self.inception9(x)
        x = F.avg_pool2d(self.pool3(x), kernel_size=7, stride=1, padding=3)
        transform = nn.AdaptiveMaxPool2d(1000)
        x = transform(x)
        return softmax0, softmax1, F.softmax(x, dim=2)






class InceptionBlock(nn.Module):
    def __init__(self, in_channels, mid_channels, out_channels):
        super(InceptionBlock, self).__init__()
        conv = Block
        self.conv1_11 = conv(in_channels=in_channels, out_channels=mid_channels, kernel=1)
        self.conv1_12 = conv(in_channels=in_channels, out_channels=mid_channels, kernel=1)
        self.pool1_1 = conv(in_channels=in_channels, out_channels=mid_channels, kernel=3, stride=1, padding=1)
        self.conv2_11 = conv(in_channels=in_channels, out_channels=out_channels, kernel=1)
        self.conv2_31 = conv(in_channels=mid_channels, out_channels=out_channels, kernel=3, padding=1)
        self.conv2_51 = conv(in_channels=mid_channels, out_channels=out_channels, kernel=5, padding=2)
        self.conv2_12 = conv(in_channels=mid_channels, out_channels=out_channels, kernel=1)

    def forward(self, x):
        first = self.conv2_11(x)
        second = self.conv1_11(x)
        second = self.conv2_31(second)
        third = self.conv1_12(x)
        third = self.conv2_51(third)
        end = F.max_pool2d(self.pool1_1(x), kernel_size=3, padding=1, stride=1)
        end = self.conv2_12(end)
        res = [first, second, third, end]
        return torch.cat(res, 1)



class AuxiliaryClassifier(nn.Module):
    def __init__(self, in_channels, out_channels):
        super(AuxiliaryClassifier, self).__init__()
        conv = Block
        self.pool = conv(in_channels, out_channels, 5, padding=2)
        self.conv1 = conv(out_channels, out_channels+16, 1)
        self.fc = nn.Linear(1000, 1)

    def forward(self, x):
        x = F.avg_pool2d(self.pool(x), kernel_size=5, stride=1, padding=1)
        x = self.conv1(x)
        adapt = nn.AdaptiveAvgPool2d(1000)
        x = adapt(x)
        x = self.fc(x)
        return F.softmax(x, dim=2)



class Block(nn.Module):
    def __init__(self, in_channels, out_channels, kernel, stride=1, padding=0):
        super(Block, self).__init__()
        self.conv = nn.Conv2d(in_channels=in_channels, out_channels=out_channels, kernel_size=kernel, stride=stride, padding=padding)
        self.batch = nn.BatchNorm2d(out_channels)

    def forward(self, x):
        x = self.conv(x)
        x = self.batch(x)
        return F.relu(x, inplace=True)
