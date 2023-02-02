import numpy as np
import pandas as pd

from sklearn.decomposition import PCA


class PrincipalComponentAnalysis:
    def __init__(self):
        self.eigenvectors = None


    def fit(self, x):
        means = np.mean(x)
        n_sample, n_features = x.shape
        data = x - means

        cov_matrix = np.dot(x.T, x)/(n_sample-1)

        vals, vectors = np.linalg.eig(cov_matrix)

        v = np.diag(vectors)

        _sort = np.sort(-v)

        atgs = np.argsort(-v)

        sorted_vectors = vectors[:, atgs]

        self.eigenvectors = np.copy(sorted_vectors)


    def transform(self, x):

        return np.dot(x, self.eigenvectors)




if __name__ == "__main__":

    df = pd.read_csv(r'breast-cancer.csv')

    x = df.iloc[:, 4:8].values

    pca = PrincipalComponentAnalysis()

    pca.fit(x)

    print(pca.transform(x))

    pca1 = PCA()

    print(pca1.fit_transform(x))