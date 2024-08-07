import torch
import torch.nn as nn

class Block(nn.Module):
    def __init__(self,input_size,output_size,use_batch_norm=True,dropout_p=.4):
        self.input_size = input_size
        self.output_size = output_size
        self.use_batch_norm = use_batch_norm
        self.dropout_p = dropout_p

        super().__init__()

        def get_regularizer(use_batch_norm, size):
            return nn.BatchNorm1d(size) if use_batch_norm else nn.Dropout(dropout_p)
        
        self.block = nn.Sequential(
            nn.Linear(input_size, output_size),
            nn.LeakyRelu(),
            get_regularizer(use_batch_norm, ouput_size)
        )
        
    def forward(self,x):
        # x : (batch_size, input_size)
        y = self.block(x)
        # y : (batch_size, output_size)
        return y
    

class ImageClassifier(nn.module):

    def __init__(self,input_size, output_size, 
                 hidden_sizes=[500,400,300,200,100], use_batch_norm=True,dropout_p=.3):
        super().__init__()
        assert len(hidden_sizes) > 0, "You need to specify hidden layers"

        last_hidden_size = input_size
        blocks = []
        for hidden_size in hidden_sizes:
            blocks += [Block(last_hidden_size, hidden_size,
                             use_batch_norm, dropout_p)]
            last_hidden_size = hidden_size

        self.layers = nn.Sequential(*blocks,
                                    nn.Linear(last_hidden_size, output_size),
                                    nn.Logsoftmax(dim=1))     #마지막 로짓값에 대한 처리는 Logsoftmax + CrossentropyLoss 혹은 softmax + NLLloss
        
        def forward(self, x):
            # x : (batch_size, input_size)
            y = self.layers(x)
            # y : (batch_size, output_size)
            # Linear layer를 통과하면 batch_size는 고정된 채 hidden_size의 차원을 조절한다.
            return y

        