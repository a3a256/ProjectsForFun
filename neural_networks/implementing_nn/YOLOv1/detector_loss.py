import torch
import numpy as np


class DetLoss:
    def __init__(self, truth_box, prediction_box):
        self.yhat = prediction_box
        self.truth = truth_box

    def get(self):
        loss = []
        for i in range(len(self.yhat)):
            _sum = []
            for j in range(1, len(self.yhat[0]), 2):
                x = self.yhat[i][j].argmax().item()
                y = self.yhat[i][j+1].argmax().item()
                true_x = self.truth[i][j-1].item()
                true_y = self.truth[i][j].item()
                if j>3:
                    x_loss = pow(x - true_x, 2)
                    y_loss = pow(y - true_y, 2)
                    _sum += [5*(x_loss+y_loss)]
                else:
                    x_loss = pow(np.sqrt(x) - np.sqrt(true_x), 2)
                    y_loss = pow(np.sqrt(y) - np.sqrt(true_y), 2)
                    _sum += [5*(x_loss+y_loss)]
            loss += [_sum]
        return torch.tensor(loss, requires_grad=True)