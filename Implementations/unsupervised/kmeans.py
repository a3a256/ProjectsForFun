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
        print(initial_centroids)

        classified = np.array(self.classify(x, initial_centroids))

        for _ in range(500):
            means = []
            for i in np.unique(classified):
                feat_ = []

                for j in range(x.shape[1]):

                    x_c = x[classified == i, j]

                    feat_ += [np.mean(x_c)]

                means += [np.array(feat_)]

            classified = self.classify(x, means)
            if self.centroids:
                # print(self.centroids)
                if not np.allclose(self.centroids, means):
                    # print(np.array(self.centroids) - np.array(means))
                    self.centroids = means
                else:
                    print("net")
                    break

            else:
                self.centroids = means
        

        self.centroids = np.array(means)
        print(self.centroids)


    def _predict(self, x):

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

                temp_cluster += [np.argmin(distances)]
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
    df = pd.read_csv(r"breast-cancer.csv")

    df.dropna(inplace=True)

    df.iloc[:, 1] = LabelEncoder().fit_transform(df.iloc[:, 1])

    y = df.iloc[:, 1].values

    x = df.iloc[:, 4:8].values

    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=0.2)


    kmeans = KMeansClustering(k=2)

    km = KMeans(n_clusters=2)


    kmeans.fit(x_train)

    km.fit(x_train)

    yhat = kmeans._predict(x_test)

    pr = km.predict(x_test)

    print(accuracy_score(yhat, y_test))

    print(accuracy_score(y_test, pr))
    print(km.cluster_centers_)

    for i in np.unique(yhat):
        plt.scatter(x_test[yhat==i, 1], x_test[yhat==i, 2])

    plt.show()
