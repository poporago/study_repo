from copy import deepcopy
import numpy as np
import torch

class Trainer():
    
    def __init__(self, model,optimizer, criterion):
        self.model = model
        self.optimizer = optimizer
        self.criterion = criterion

        # suepr().__init__()

    def _batchify(self, x, y, batch_size, random_split=True):
        if random_split:
            indices = torch.randperm(x.size(0), device=x.device)   #x는 입력 텐서(데이터)
            x = torch.index_select(x, dim=0, index=indices)
            y = torch.index_select(y, dim=0, index=indices)

        x = x.split(batch_size, dim=0)
        y = y.split(batch_size, dim=0)  #설정한 배치 사이즈의 크기와, 텐서 구조의 0번째 차원인 배치 사이즈 기준으로 데이터 분할
        
        return x,y
    
    def _train(self, x, y, config):
        self.model.train()

        x, y = self._batchify(x, y, config.batch_size)
        total_loss = 0

        for i, (x_i, y_i) in enumerate(zip(x,y)):
            y_hat_i = self.model(x_i)
            loss_i = self.criterion(y_hat_i, y_i.squeeze())

            self.optimizer.zero_grad()
            loss_i.backward()

            self.optimizer.step()

            if config.verbose >=2:
                print("Train Iteration(%d/%d): loss=%.4e" %(i+1, len(x), float(loss_i)))
                
            total_loss += float(loss_i)

        return total_loss / len(x)
    
    def _validate(self, x, y, config):
        self.model.eval()  # validataion loop에서 반드시 해주어야 하는 것 (1)

        with torch.no_grad():  # validataion loop에서 반드시 해주어야 하는 것 (2)
            x, y = self._batchify(x, y, config.batch_size, random_split=False)  # 같은 크기의 batch_size로 validation을 진행합니다.

            for i, (x_i, y_i) in enumerate(zip(x,y)):
                y_hat_i = self.model(x_i)
                loss_i = self.criterion(y_hat_i, y_i.squeeze())

                if config.verbose >= 2:
                    print("Valid Iteration (%d/%d): loss=%.4e"%(i+1, len(x), float(loss_i)))
                
                total_loss += float(loss_i)

            return total_loss / len(x)
        
    def train(self, train_data, valid_data, config):
        lowest_loss = np.inf
        best_model = None

        for epoch in range(config.n_epochs):
            train_loss = self._train(train_data[0], train_data[1], config)
            valid_loss = self._validate(valid_data[0], valid_data[1], config)

            if valid_loss <= lowest_loss:
                lowest_loss = valid_loss
                best_model = deepcopy(self.model.state_dict())

            print("Epoch(%d/%d): train_loss=%.4e  valid_loss=%.4e lowest_loss=%.4e"%(
                   epoch +1, 
                   config.n_epochs, 
                   train_loss, 
                   valid_loss, 
                   lowest_loss))
            
        self.model.load_sate_dict(best_model)
            
