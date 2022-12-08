import torch.nn as nn
import pandas as pd
import numpy as np
import torch
import torchvision.transforms as transforms
from torch.utils.data import DataLoader, Dataset
import torchvision
import torch.functional as F
import matplotlib.image as img
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import time
from inception_attempt import Inception

df = pd.read_csv(r'train.csv')
test = pd.read_csv(r'test.csv')

for i in range(len(df)):
    df.iloc[i, 0] = "Train images/"+df.iloc[i, 0]

for i in range(len(test)):
    test.iloc[i, 0] = "Test images/"+test.iloc[i, 0]

df = df.iloc[35:50, :]
df.drop(43, inplace=True)
df.drop(47, inplace=True)


le = LabelEncoder()
df.iloc[:, 1] = le.fit_transform(df.iloc[:, 1])

class SplitDataset(Dataset):
    def __init__(self, data, transform=None):
        super().__init__()
        self.data = data.values
        self.transform = transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        img_path, label = self.data[index]
        image = img.imread(img_path)
        if self.transform is not None:
            image = self.transform(image)

        return image, label


train, valid = train_test_split(df, test_size=0.2)
size = 32
train_transform = transforms.Compose([transforms.ToPILImage(),
                                    transforms.Resize((size, size)),
                                    transforms.ToTensor(),
                                    transforms.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225))])

valid_transform = transforms.Compose([transforms.ToPILImage(),
                                    transforms.Resize((size, size)),
                                    transforms.ToTensor(),
                                    transforms.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225))])

train_split = SplitDataset(train, train_transform)
valid_split = SplitDataset(valid, valid_transform)

bath_size = 2
epochs = 3

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

train_ds = DataLoader(train_split, batch_size=bath_size, shuffle=True)
valid_ds = DataLoader(valid_split, batch_size=bath_size, shuffle=False)

model = Inception(4)
model = model.to(device)

criterion = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

for i in range(epochs):
    train_loss = []
    test_loss = []
    model.train()
    for data, label in train_ds:
        out = model(data.to(device))
        out = out.view(out.shape[0], -1)
        loss = criterion(out, label.to(device))
        train_loss += [loss.item()]
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    model.eval()
    for data, label in valid_ds:
        out = model(data.to(device))
        out = out.view(out.shape[0], -1)
        loss = criterion(out, label.to(device))
        test_loss += [loss.item()]

    print("Epoch {} \ttrain loss: {}, \ttest_loss: {}".format(i+1, np.mean(train_loss), np.mean(test_loss)))
# torch.save(model.state_dict(), "inception_classifier_model.pt")