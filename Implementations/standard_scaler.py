import pandas as pd

def std(arr):
    new_arr = []
    mean = sum(arr)/len(arr)
    for i in arr:
        new_arr += [(i-mean)**2]
    return (sum(new_arr)/len(arr))**(0.5)

def mean(arr):
    return sum(arr)/len(arr)

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


class ZNormalization:
    def __init__(self):
        self.stds = None
        self.means = None

    def fit(self, x):
        self.stds = []
        self.means = []
        if len(x.shape) > 1:
            for i in range(x.shape[1]):
                self.stds += [std(x[:, i])]
                self.means += [mean(x[:, i])]
        else:
            self.stds += [std(x)]
            self.means += [mean(x)]

    def transform(self, x):
        n_samples, n_features = 0, 0
        if len(x.shape)>1:
            n_samples, n_features = x.shape
        else:
            n_samples = x.shape[0]
        if n_features>1:
            for i in range(n_samples):
                for j in range(n_features):
                    x[i, j] = (x[i, j]-self.means[j])/(self.stds[j])
        else:
            for i in range(n_samples):
                x[i] = ((x[i]-self.means[0])/(self.stds[0]))
        return x


if __name__ == "__main__":
    df = pd.read_csv(r'ready_for_nn.csv')
    # sc = StandardScaler()
    # sc.fit(df.iloc[:, [0,2]].values)
    # print(df.iloc[:10, [0,2]].values)
    # print(sc.transform(df.iloc[:10, [0,2]].values))
    # print(sc.inverse_transform(sc.transform(df.iloc[:10, [0,2]].values)))
    sc = ZNormalization()
    sc.fit(df.iloc[:, [0,2]].values)
    print(df.iloc[:10, [0,2]].values)
    print(sc.transform(df.iloc[:10, [0,2]].values))
    print(df.iloc[:10, 0].values)
    sc.fit(df.iloc[:, 0].values)
    print(sc.transform(df.iloc[:10, 0].values))
    # print(sc.inverse_transform(sc.transform(df.iloc[:10, [0,2]].values)))
