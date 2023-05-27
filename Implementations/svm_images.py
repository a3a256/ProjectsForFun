import numpy as np
import pandas as pd
from PIL import Image
from skimage.transform import resize


class SVM:
    def __init__(self, num_classes, im_size, lr=0.1, epochs=20):
        self.lr = lr
        self.size = im_size
        self.linear = None
        self.fc = None
        self.last = None
        self.epochs = 20
        self.classes = num_classes


    def cross_entropy(self, x, y):
        
        pass


    def fit(self, x, y):
        nsamples = x.shape[0]

        self.linear = np.random.rand(self.size, 1024)
        self.fc = np.random.rand(1024, self.classes)
        self.last = np.random.rand(1024, 1)

        backup = [self.linear, self.fc, self.last]

        for _ in range(self.epochs):

            for i in range(nsamples):
                image = Image.open("Train images/"+x[i]).convert("L")
                image = np.asarray(image)
                image = resize(image, (self.size, self.size))

                pred1 = np.dot(image, self.linear)
                pred2 = np.dot(self.linear, self.fc)
                final = np.dot(self.fc.T, self.last)

                print(final.shape)
                print(final)

                break
            break
        
        return
    


if __name__ == '__main__':
    df = pd.read_csv('train.csv')

    ml = SVM(4, 224)

    ml.fit(df.iloc[:, 0], df.iloc[:, -1])