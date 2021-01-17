import csv
import torch
from torch import nn, optim 
from torch.utils.data import Dataset, DataLoader, random_split

import numpy as np
from matplotlib import pyplot as plt

from tqdm import tqdm

from make_dictionary import build_dictionary
from dataset import MyDataset, load_data
from model import Model

device = torch.device('cpu')

def split_data():
    word2token, token2word = build_dictionary()
    input_data, label_data = load_data(word2token)
    dataset = MyDataset(input_data, label_data)
  
    # データセット分割
    n_samples = len(dataset)
    val_size = int(n_samples*0.1)
    train_size = n_samples - val_size
    train_dataset, val_dataset = random_split(dataset, [train_size, val_size], generator=torch.Generator().manual_seed(1))
    train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=32, shuffle=True)
    return train_dataset, val_dataset, train_loader, val_loader

# モデル評価
def eval_net(model, data_loader, loss, device):
    model.eval()
    model = model.to(device)
    outputs = []
    accs = []
    for i, (input_feature, label) in enumerate(data_loader):
        with torch.no_grad():
            # GPU setting
            input_feature = input_feature.to(device)
            label = label.to(device)
    
        # モデルの推測
        pred = model(input_feature)
        # シグモイドで0-1に正規化
        m = nn.Sigmoid()
        # 交差エントロピー
        pred = torch.squeeze(m(pred))
        output = loss(pred, label)
        
        # 最大値のインデックスを取得
        _, idx = torch.max(pred, 1)
        
        # tensorからnumpyに変換
        idx = idx.to('cpu').detach().numpy().copy()
        label = label.to('cpu').detach().numpy().copy()
        # 精度計算
        acc = (idx == label).sum() / len(label)            
        accs.append(acc)

    return sum(outputs) / i , sum(accs)/i
    

# モデルの学習
def train_net(model, train_loader, valid_loader, loss, n_iter, device):
    train_losses = []
    valid_losses = []
    train_accs = []
    val_accs = []
    optimizer = optim.Adam(model.parameters())
    for epoch in range(n_iter):
        running_loss = 0.0
        model = model.to(device)
        # ネットワーク訓練モード
        model.train()
        accs = []
        for i, (input_feature, label) in enumerate(train_loader):        
            # GPU setting
            input_feature = input_feature.to(device)
            label = label.to(device)

            # モデルの推測
            pred = model(input_feature)
            # シグモイドで0-1に正規化
            m = nn.Sigmoid()
            # 交差エントロピー
            pred = torch.squeeze(m(pred))
            output = loss(pred, label)
         
            # 最大値のインデックスを取得
            _, idx = torch.max(pred, 1)
            
            # tensorからnumpyに変換
            idx = idx.to('cpu').detach().numpy().copy()
            label = label.to('cpu').detach().numpy().copy()
            # 精度計算
            acc = (idx == label).sum() / len(label)            
            accs.append(acc)
            
   
            optimizer.zero_grad()
            output.backward()
            optimizer.step()
            running_loss += output.item()
    
        # 訓練用データでのloss値
        train_losses.append(running_loss / i)
        # 検証用データでのloss値
        pred_valid, val_acc =  eval_net(model, valid_loader, loss, device)
        train_accs.append(sum(accs)/i)
        val_accs.append(val_acc)
        valid_losses.append(pred_valid)
        print('epoch:' +  str(epoch+1), 'train loss:'+ str(train_losses[-1]), 'valid loss:' + str(valid_losses[-1]), 'train acc:' + str(train_accs[-1]),  'val acc:' + str(val_accs[-1]), flush=True)

        # 学習モデル保存
        if (epoch+1)%1==0:
            # 学習させたモデルの保存パス
            model_path =  f'model/epoch{epoch+1}.pth'
            # モデル保存
            torch.save(model.to('cpu').state_dict(), model_path)
            # グラフ描画
            my_plot(train_losses, valid_losses)
    return train_losses, valid_losses

def my_plot(train_losses, valid_losses):
    # グラフの描画先の準備
    fig = plt.figure()
    # 画像描画
    plt.plot(train_losses, label='train')
    plt.plot(valid_losses, label='valid')
    #グラフタイトル
    plt.title('Triplet Margin Loss')
    #グラフの軸
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    #グラフの凡例
    plt.legend()
    # グラフ画像保存
    fig.savefig("loss.png")

def select_epoch(valid_losses):
    min_loss = min(valid_losses)
    return valid_losses.index(min_loss) + 1

def main():
    _, _, train_loader, val_loader = split_data()
    model = Model()
    loss = nn.CrossEntropyLoss()
    print("訓練開始")
    _, valid_losses = train_net(model=model, 
                                           train_loader=train_loader, 
                                           valid_loader=val_loader,  
                                           loss=loss, 
                                           n_iter=10, 
                                           device=device)
    best_epoch = select_epoch(valid_losses)
    print(f'{best_epoch}epochのモデルが最もvalid lossが下がった。')
    
    return None


if __name__ == '__main__':
    main()