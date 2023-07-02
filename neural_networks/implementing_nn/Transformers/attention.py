import numpy as np
import math
import torch
from nltk import tokenize

def positional_encoding(seq_len, d=512, n=10000):
    res = []
    for i in range(seq_len):
        temp = []
        for j in range(d//2):
            temp += [np.sin(i/(n**(2*j/d)))]
            temp += [np.cos(i/(n**(2*j/d)))]

        res += [temp]

    return torch.Tensor(res).type(torch.FloatTensor)



class PosEncoding(torch.nn.Module):
    def __init__(self, vocab_size, embed_dim, sequence_len):
        super(PosEncoding, self).__init__()
        self.embed = torch.nn.Embedding(vocab_size, embed_dim)
        self.d_model = sequence_len

    def forward(self, x, offsets):
        x = self.embed(x, offsets)
        y = positional_encoding(self.d_model)
        return torch.add(x, torch.Tensor(y))


class AttentionLayer(torch.nn.Module):
    def __init__(self, embed_dim, num_heads, dropout):
        super(AttentionLayer, self).__init__()
        self.mha = torch.nn.MultiheadAttention(embed_dim, num_heads=num_heads, dropout=dropout)
        self.norm = torch.nn.LayerNorm()


class FFNN(torch.nn.Module):
    def __init__(self, embed_dims, output_dims, rate=0.1):
        super(FFNN, self).__init__()
        self.layer1 = torch.nn.Linear(embed_dims, output_dims)
        self.activate = torch.nn.ReLU(inplace=True)
        self.layer2 = torch.nn.Linear(output_dims, embed_dims)
        self.drop = torch.nn.Dropout(rate, inplace=True)
        self.norm = torch.nn.LayerNorm()

    def forward(self, x):
        y = self.layer1(x)
        y = self.activate(x)
        y = self.layer2(x)
        y = self.drop(x)
        x = torch.add(x, y)
        return self.norm(x)


class EncoderAttention(AttentionLayer):
    '''
    Add and normalize tensors
    '''
    def forward(self, x):
        y = self.mha(x, x, x)
        x = torch.add(x, y)
        return self.norm(x)


class DecoderAttention(AttentionLayer):
    def forward(self, x):
        return self.norm(torch.add(x, self.mha(x, x, x)))

    
class EncoderLayer(torch.nn.Module):
    def __init__(self, embed_dim, output_dims, num_heads, dropout):
        super(EncoderLayer, self).__init__()
        self.attention = EncoderAttention(embed_dim, num_heads, dropout)
        self.ffn = FFNN(embed_dim, output_dims)

    def forward(self, x):
        return self.ffn(self.attention(x))
    


class Encoder(torch.nn.Module):
    def __init__(self, n_layers, embed_dim, output_dims, num_heads, dropout, vocab_size):
        super(Encoder, self).__init__()
        self.num_layers = n_layers
        self.pos_encoding = PosEncoding(vocab_size, embed_dim, 2048)
        self.layers = [EncoderLayer(embed_dim, output_dims, num_heads, dropout)
                       for _ in range(n_layers)]
        
    def forward(self, x):
        x = self.pos_encoding(x)

        for i in range(self.num_layers):
            x = self.layers[i](x)

        return x



class CrossAttention(AttentionLayer):
    def forward(self, x, context):
        attention_layer, attention_scores = self.mha(x, context, context)

        self.last_attn_scores = attention_scores

        x = torch.add(x, attention_layer)

        return self.norm(x)
    

class DecoderLayer(torch.nn.Module):
    def __init__(self, embed_dim, output_dims, num_heads, dropout):
        super(DecoderLayer, self).__init__()
        self.decode = DecoderAttention(embed_dim, num_heads, dropout)
        self.cross_attention = CrossAttention(embed_dim, num_heads, dropout)
        self.ffn = FFNN(embed_dim, output_dims)

    def forward(self, x, context):
        x = self.decode(x)

        x = self.cross_attention(x, context)

        self.last_attention_scores = self.cross_attention.last_attn_scores

        x = self.ffn(x)

        return x
    

class Decoder(torch.nn.Module):
    def __init__(self, n_layers, embed_dims, output_dims, num_heads, dropout, vocab_size):
        super(Decoder, self).__init__()

        self.pos_encoder = PosEncoding(vocab_size, embed_dims, 2048)

        self.layers = [DecoderLayer(embed_dims, output_dims, num_heads, dropout)
                       for _ in range(n_layers)]
        
        self.n_layers = n_layers

    def forward(self, x, context):
        x = self.pos_encoder(x)

        for i in range(self.n_layers):
            x = self.layers[i](x)


        return x




word = '''
In languages, the order of the words and their position in a sentence really matters. 
The meaning of the entire sentence can change if the words are re-ordered. 
When implementing NLP solutions, recurrent neural networks have an inbuilt mechanism that deals with the order of sequences. 
The transformer model, however, does not use recurrence or convolution and treats each data point as independent of the other. 
Hence, positional information is added to the model explicitly to retain the information regarding the order of words in a sentence. 
Positional encoding is the scheme through which the knowledge of the order of objects in a sequence is maintained.
'''

length = len(word.split())

# print(positional_encoding(length, 5, 100))

# ml = PosEncoding(128, 512, 2048)

indices = [475, 21, 30, 5297]

indices = torch.Tensor(indices).type(torch.LongTensor)

print(positional_encoding(2048).shape)


# print(ml(indices))
