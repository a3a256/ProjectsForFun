import torch
from googlenet import GoogLeNet

model = GoogLeNet(4)
model = model.to(device)

criterion = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

for i in range(epochs):
    train_loss = []
    test_loss = []
    model.train()
    for data, label in train_ds:
        out = model(data.to(device))
        loss1, loss2, loss3 = out
        # print(loss1.shape)
        # print(loss2.shape)
        # print(loss3.shape)
        outs = loss1+loss2+loss3
        outs = outs.view(outs.shape[0], -1)
        loss = criterion(outs, label.to(device))
        train_loss += [loss.item()]
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    model.eval()
    for data, label in valid_ds:
        out = model(data.to(device))
        outs = out[0]+out[1]+out[2]
        outs = outs.view(outs.shape[0], -1)
        loss = criterion(outs, label.to(device))
        test_loss += [loss.item()]

    print("Epoch {} \ttrain loss: {}, \ttest_loss: {}".format(i+1, np.mean(train_loss), np.mean(test_loss)))
