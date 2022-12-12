import torch
import torch.nn as nn
import torch.nn.functional as F

class ResNet34(nn.Module):
    def __init__(self):
        super(ResNet34, self).__init__()
        conv = BlockCNN
        self.conv1 = Conv1(in_channels=3, out_channels=64)
        self.conv2 = Conv2(64)
        self.conv3 = Conv3(64, 128)
        self.conv4 = Conv4(128, 256)
        self.conv5 = Conv5(256, 512)
        self.end = EndLayer()

    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = self.conv3(x)
        x = self.conv4(x)
        x = self.conv5(x)
        x = self.end(x)
        return x



class Conv1(nn.Module):
    def __init__(self, in_channels, out_channels, stride=1, padding=0):
        super(Conv1, self).__init__()
        conv = BlockCNN
        self.layer = conv(in_channels, out_channels, 7, stride=2, padding=padding)

    def forward(self, x):
        x = self.layer(x)
        x = F.max_pool2d(x, kernel_size=3, stride=2)
        return F.relu(x, inplace=True)


class Conv2(nn.Module):
    def __init__(self, out_channels, kernel=3, stride=1, padding=1):
        super(Conv2, self).__init__()
        conv = BlockCNN
        self.branch = nn.Sequential(conv(out_channels, out_channels, kernel, stride, padding),
                                    nn.ReLU(inplace=True),
                                    conv(out_channels, out_channels, kernel, stride, padding))
    
    def forward(self, x):
        fx1 = self.branch(x)
        fx1 = fx1 + x
        fx2 = self.branch(fx1)
        fx2 = fx2 + fx1
        fx3 = self.branch(fx2)
        residual = fx3 + fx2
        return F.relu(residual, inplace=True)


class Conv3(nn.Module):
    def __init__(self, in_channels, out_channels, kernel=3, stride=1, padding=1):
        super(Conv3, self).__init__()
        conv = BlockCNN
        self.increment = nn.Sequential(conv(in_channels, out_channels, kernel, stride, 0),
                                    nn.ReLU(inplace=True),
                                    conv(out_channels, out_channels, kernel, stride, 0))
        self.branch = nn.Sequential(conv(out_channels, out_channels, kernel, stride, padding),
                                    nn.ReLU(inplace=True),
                                    conv(out_channels, out_channels, kernel, stride, padding))

    def forward(self, x):
        x = self.increment(x)
        x = F.relu(x, inplace=True)
        fx1 = self.branch(x)
        fx1 = fx1 + x
        fx2 = self.branch(fx1)
        fx2 = fx2 + fx1
        fx3 = self.branch(x)
        fx3 = fx3 + fx2
        return F.relu(fx3, inplace=True)


class Conv4(nn.Module):
    def __init__(self, in_channels, out_channels, kernel=3, stride=1, padding=1):
        super(Conv4, self).__init__()
        conv = BlockCNN
        self.increment = nn.Sequential(conv(in_channels, out_channels, kernel, stride, 0),
                                    nn.ReLU(inplace=True),
                                    conv(out_channels, out_channels, kernel, stride, 0))
        self.branch = nn.Sequential(conv(out_channels, out_channels, kernel, stride, padding),
                                    nn.ReLU(inplace=True),
                                    conv(out_channels, out_channels, kernel, stride, padding))

    def forward(self, x):
        x = self.increment(x)
        x = F.relu(x, inplace=True)
        fx1 = self.branch(x)
        fx1 = fx1 + x
        fx2 = self.branch(fx1)
        fx2 = fx2 + fx1
        fx3 = self.branch(x)
        fx3 = fx3 + fx2
        fx4 = self.branch(fx3)
        fx4 = fx4 + fx3
        fx5 = self.branch(fx4)
        fx5 = fx5 + fx4
        return F.relu(fx5, inplace=True)


class Conv5(nn.Module):
    def __init__(self, in_channels, out_channels, kernel=3, stride=1, padding=1):
        super(Conv5, self).__init__()
        conv = BlockCNN
        self.increment = nn.Sequential(conv(in_channels, out_channels, kernel, stride, 0),
                                    nn.ReLU(inplace=True),
                                    conv(out_channels, out_channels, kernel, stride, 0))
        self.branch = nn.Sequential(conv(out_channels, out_channels, kernel, stride, padding),
                                    nn.ReLU(inplace=True),
                                    conv(out_channels, out_channels, kernel, stride, padding))

    def forward(self, x):
        x = self.increment(x)
        x = F.relu(x, inplace=True)
        fx1 = self.branch(x)
        fx1 = fx1 + x
        fx2 = self.branch(fx1)
        fx2 = fx2 + fx1
        return F.relu(fx2, inplace=True)


class EndLayer(nn.Module):
    def __init__(self):
        super(EndLayer, self).__init__()
        self.fc = nn.Linear(1000, 1)
    
    def forward(self, x):
        x = F.avg_pool2d(x, kernel_size=1)
        ref = nn.AdaptiveAvgPool2d(1000)
        x = ref(x)
        return F.softmax(self.fc(x), dim=2)



class BlockCNN(nn.Module):
    def __init__(self, in_channels, out_channels, kernel, stride=1, padding=0):
        super(BlockCNN, self).__init__()
        self.conv = nn.Conv2d(in_channels=in_channels, out_channels=out_channels, kernel_size=kernel, stride=stride, padding=padding)
        self.batch = nn.BatchNorm2d(out_channels)

    def forward(self, x):
        return F.relu(self.batch(self.conv(x)), inplace=True)
