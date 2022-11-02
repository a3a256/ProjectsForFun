import pandas as pd

class StandardScaler:
    def __init__(self):
        self.min_x = None
        self.max_x = None

    def fit(self, x):
        if x.shape[1] > 1:
            self.min_x = []
            self.max_x = []
            for i in range(x.shape[1]):
                self.min_x += [min(x[:, i])]
                self.max_x += [max(x[:, i])]
        else:
            self.min_x = min(x)
            self.max_x = max(x)
        print(self.min_x)
        print(self.max_x)

    def transform(self, x):
        if x.shape[1] > 1:
            for i in range(x.shape[1]):
                for j in range(x.shape[0]):
                    x[j, i] = (x[j, i]-self.min_x[i])/(self.max_x[i] - self.min_x[i])
        else:
            for i in range(len(x)):
                x[i] = (x[i]-self.min_x)/(self.max_x-self.min_x)
        
        return x

    def inverse_transform(self, x):
        if x.shape[1] > 1:
            for i in range(x.shape[1]):
                for j in range(x.shape[0]):
                    x[j, i] = (x[j, i]*(self.max_x[i]-self.min_x[i])) + self.min_x[i]
        else:
            for i in range(len(x)):
                x[i] = (x[i]*(self.max_x-self.min_x)) + self.min_x
        
        return x


if __name__ == "__main__":
    df = pd.read_csv(r'ready_for_nn.csv')
    sc = StandardScaler()
    sc.fit(df.iloc[:, [0,2]].values)
    print(df.iloc[:10, [0,2]].values)
    print(sc.transform(df.iloc[:10, [0,2]].values))
    print(sc.inverse_transform(sc.transform(df.iloc[:10, [0,2]].values)))
