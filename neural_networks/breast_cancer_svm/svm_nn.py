import torch
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

class SVM(torch.nn.Module):
    def __init__(self, n_features):
        super(SVM, self).__init__()
        self.ln1 = torch.nn.Linear(n_features, 1)
        self.fc = torch.nn.ReLU()

    def forward(self, x):
        return self.fc(self.ln1(x))

class NNSVM:
    def __init__(self, epochs):
        self.model = None
        self.epochs = epochs


    def fit(self, x, y):
        dims = x.shape
        n_features = 0
        if len(dims) == 1:
            n_features = 1
        else:
            n_features = x.shape[1]
        x = torch.Tensor(x).type(torch.FloatTensor)
        y = torch.Tensor(y).type(torch.FloatTensor)
        self.model = SVM(n_features)
        criterion = torch.nn.HingeEmbeddingLoss()
        optimizer = torch.optim.SGD(self.model.parameters(), lr=0.01)
        self.model.train()
        for i in range(self.epochs):
            out = self.model(x)
            loss = criterion(out, y)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            print("Epoch {} loss: {}".format(i+1, loss.item()))

    def predict(self, x):
        x = torch.Tensor(x).type(torch.FloatTensor)
        out = self.model(x).detach().numpy()
        res = [1 if i > 0 else 0 for i in out]
        return res


if __name__ == "__main__":
    df = pd.read_csv(r'pima-indians-diabetes.csv')
    le = LabelEncoder()
    sc = StandardScaler()
    x = df.iloc[:, :-1].values
    x = sc.fit_transform(x)
    y = df.iloc[:, -1].values
    y = le.fit_transform(y)
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=0.2)
    ml = NNSVM(20)
    ml.fit(x_train, y_train)
    y_hat = ml.predict(x_test)
    print(accuracy_score(y_hat, y_test))