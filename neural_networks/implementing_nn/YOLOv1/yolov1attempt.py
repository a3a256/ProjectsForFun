import torch
import torch.nn as nn
import torch.nn.functional as F


class yolo(nn.Module):
    def __init__(self):
        super(yolo, self).__init__()
        self.layer1 = CNN1()
        self.layer2 = CNN2()
        self.layer3 = CNN3()
        self.layer4 = CNN4()
        self.layer5 = CNN5()
        self.fc1 = nn.Linear(1024, 4096)
        self.fc2 = nn.Linear(4096, 5)

    def forward(self, x):
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.layer4(x)
        x = self.layer5(x)
        x = x.view(x.shape[0], x.shape[2], x.shape[3], x.shape[1])
        x = self.fc1(x)
        x = self.fc2(x)
        x = x.view(x.shape[0], x.shape[3], x.shape[1], x.shape[2])
        return F.relu(x, inplace=True)



class CNN1(nn.Module):
    def __init__(self):
        super(CNN1, self).__init__()
        block = BlockCNN
        self.conv = block(3, 64, 7, 1, 3)
        self.pool = block(64, 64, 2, 2, 1)

    def forward(self, x):
        x = self.conv(x)
        x = F.max_pool2d(self.pool(x), kernel_size=2, stride=2)
        return F.relu(x, inplace=True)


class CNN2(nn.Module):
    def __init__(self):
        super(CNN2, self).__init__()
        block = BlockCNN
        self.conv = block(64, 192, 3, 1, 1)
        self.pool = block(192, 192, 2, 1, 1)

    def forward(self, x):
        x = self.conv(x)
        x = F.max_pool2d(self.pool(x), kernel_size=2, stride=2)
        return F.relu(x, inplace=True)


class CNN3(nn.Module):
    def __init__(self):
        super(CNN3, self).__init__()
        block = BlockCNN
        self.branch = nn.Sequential(block(192, 128, 1),
                                    block(128, 256, 3, 1, 1),
                                    block(256, 256, 1),
                                    block(256, 512, 3, 1, 1))
        self.pool = block(512, 512, 2, 1, 1)

    def forward(self, x):
        x = self.branch(x)
        x = F.max_pool2d(self.pool(x), kernel_size=2, stride=2)
        return F.relu(x, inplace=True)


class CNN4(nn.Module):
    def __init__(self):
        super(CNN4, self).__init__()
        block = BlockCNN
        self.first_branch = nn.Sequential(block(512, 256, 1),
                                    block(256, 512, 3, 1, 1))
        self.second_branch = nn.Sequential(block(512, 512, 1),
                                    block(512, 1024, 3, 1, 1),
                                    block(1024, 1024, 2, 1, 1))

    def forward(self, x):
        for i in range(4):
            x = self.first_branch(x)
        x = self.second_branch(x)
        x = F.max_pool2d(x, kernel_size=2, stride=2)
        return F.relu(x, inplace=True)


class CNN5(nn.Module):
    def __init__(self):
        super(CNN5, self).__init__()
        block = BlockCNN
        self.first_branch = nn.Sequential(block(1024, 512, 1),
                                        block(512, 1024, 3, 1, 1))
        self.second_branch = nn.Sequential(block(1024, 1024, 3, 1, 1), block(1024, 1024, 3, 2, 1))

    def forward(self, x):
        x = self.first_branch(x)
        x = self.first_branch(x)
        x = self.second_branch(x)
        return F.relu(x, inplace=True)


class BlockCNN(nn.Module):
    def __init__(self, in_channels, out_channels, kernel, stride=1, padding=0):
        super(BlockCNN, self).__init__()
        self.conv = nn.Conv2d(in_channels, out_channels, kernel_size=kernel, stride=stride, padding=padding)
        self.batch = nn.BatchNorm2d(out_channels)

    def forward(self, x):
        x = self.conv(x)
        x = self.batch(x)
        # print(x.shape)
        return F.relu(x, inplace=True)
