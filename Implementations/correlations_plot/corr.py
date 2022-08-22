class Correlation:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mean(self, x):
        return sum(x)/len(x)

    def std(self, x):
        mean = self.mean(x)
        upper = sum([(i - mean)**2 for i in x])
        return (upper/len(x))**(1/2)

    def correlate(self):
        mean_x = self.mean(self.x)
        mean_y = self.mean(self.y)
        upper = 0
        for i in range(len(self.x)):
            upper += (self.x[i] - mean_x)*(self.y[i] - mean_y)
        covariance = upper/len(self.x)
        corr = (covariance)/((self.std(self.x))*self.std(self.y))
        return corr