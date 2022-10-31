import torch
import torch.nn as nn
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

df = pd.read_csv(r'ready_for_nn.csv')

x = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=0.2)

print(torch.Tensor([[1]]))

x_data = torch.Tensor(x_train)
y_data = torch.Tensor(y_train)


class LinearRegressionModel(torch.nn.Module):
    def __init__(self):
        super(LinearRegressionModel, self).__init__()
        self.linear = torch.nn.Linear(5, 1)

    def forward(self, x):
        y_pred = self.linear(x)