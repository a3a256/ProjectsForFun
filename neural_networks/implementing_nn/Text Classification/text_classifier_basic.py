import torch


class TextClassifier(torch.nn.Module):
    def __init__(self, vocab_size, embed_dim, num_class):
        super(TextClassifier, self).__init__()
        self.embed = torch.nn.EmbeddingBag(vocab_size, embed_dim, sparse=True)
        self.fc = torch.nn.Linear(embed_dim, num_class)

    def init_weights(self):
        initrange = 0.5
        self.embed.weight.data.uniform_(-initrange, initrange)
        self.fc.weight.data.uniform_(-initrange, initrange)
        self.fc.bias.data.zero_()

    def forward(self, text, label):
        embedded = self.embed(text, label)
        return self.fc(embedded)