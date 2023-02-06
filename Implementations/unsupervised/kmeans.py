import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from collections import Counter

from sklearn.model_selection import train_test_split


class KMeansClustering:
    def __init__(self, init='random', k=1):
        self.k = k
        self.init = init
        self.centroids = None


    def distance(self, x, y):
        return abs(x - y)


    def fit(self, x):

        initial_centroids = self.split(x)

        classified = np.array(self.classify(x, initial_centroids))

        for _ in range(20):
            means = []
            for i in np.unique(classified):
                feat_ = []

                for j in range(x.shape[1]):

                    x_c = x[classified == i, j]

                    feat_ += [np.mean(x_c)]

                means += [np.array(feat_)]

            classified = self.classify(x, means)

        self.centroids = np.array(means)
        print(self.centroids)


    def predict(self, x):

        return self.classify(x, self.centroids)


    def classify(self, x, centroids):

        n_samples, n_features = x.shape

        clustered = []


        for i in range(n_samples):
            temp_cluster = []
            for j in range(n_features):
                distances = []
                for k in range(self.k):
                    distances += [self.distance(x[i, j], centroids[k][j])]

                temp_cluster += [np.argmax(distances)]
            classes = Counter(temp_cluster)

            c = sorted(classes, key = lambda x: (-classes[x]))

            clustered += [c[0]]

        return clustered

                


    def split(self, x):

        n_samples, n_features = x.shape

        centroids = []

        for i in range(self.k):
            centroids += [x[i, :]]

        return centroids




if __name__ == "__main__":
    df = pd.read_csv(r'breast-cancer.csv')

    y = df.iloc[:, 1].values

    y = LabelEncoder().fit_transform(y)

    x = df.iloc[:, 4:8].values

    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=0.2)


    kmeans = KMeansClustering(k=2)


    kmeans.fit(x_train)

    yhat = kmeans.predict(x_test)

    print(accuracy_score(yhat, y_test))

    for i in np.unique(yhat):
        plt.scatter(x_test[yhat==i, 0], x_test[yhat==i, 1])

    plt.show()