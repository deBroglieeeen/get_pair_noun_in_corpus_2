import torch
from torch import nn, optim 
from torch.utils.data import Dataset, DataLoader

from model import Model
from dataset import MyDataset
from train import split_data

from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score

# GPU対応
device = torch.device('cpu')

def load_model():
    # 学習済みモデル読み込み
    model = Model()
    model.load_state_dict(torch.load('model/epoch800.pth', map_location=device))
    return model

def load_testdata():
    return 

def eval(model, test_loader, device):
    model = model.to(device)
    model.eval()
    pred_list = []
    label_list = []
    for i, (input_feature, label) in enumerate(test_loader):
        with torch.no_grad():
            # GPU setting
            print(input_feature)
            input_feature = input_feature.to(device)
            label = label.to(device)
    
        # モデルの推測
        pred = model(input_feature)
        print('それぞれの確率値:', pred)
        
        # 最大値のインデックスを取得
        _, idx = torch.max(pred, 1)
        
        # tensorからnumpyに変換
        idx = idx.to('cpu').detach().numpy().copy().tolist()
        label = label.to('cpu').detach().numpy().copy().tolist()

        print('それぞれの確率の中の最大値のインデックスが予測ラベル:', idx)
        print('真のラベル:', label)

        pred_list += idx 
        label_list += label

        if i == 0:
            break
    return pred_list, label_list

def main():
    # データロード
    _, val_dataset, _, _ = split_data()
    print('テスト用データ数:', len(val_dataset))
    val_loader = DataLoader(val_dataset, batch_size=3000, shuffle=False)
    # モデルロード
    model = load_model()
    # 予測ラベルと真のラベル
    pred_list, label_list = eval(model, val_loader,  device)

    # # F1値のマクロ平均出力
    f1 = f1_score(label_list, pred_list, average='micro')
    print("F1score:", f1)
    

    return None

if __name__ == '__main__':
    main()