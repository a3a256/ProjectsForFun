import pandas as pd

class StandardScaler:
    def __init__(self):
        self.min_x = None
        self.max_x = None

    def fit(self, x):
        self.min_x = min(x)
        self.max_x = max(x)

    def transform(self, x):
        for i in range(len(x)):
            x[i] = (x[i]-self.min_x)/(self.max_x - self.min_x)
        
        return x

    def inverse_transform(self, x):
        for i in range(len(x)):
            x[i] = (x[i]*(self.max_x-self.min_x)) + self.min_x
        
        return x


if __name__ == "__main__":
    df = pd.read_csv(r'ready_for_nn.csv')
    sc = StandardScaler()
    sc.fit(df.iloc[:, 2].values)
    print(df.iloc[:10, 2].values)
    print(sc.transform(df.iloc[:10, 2].values))
    print(sc.inverse_transform(df.iloc[:10, 2].values))