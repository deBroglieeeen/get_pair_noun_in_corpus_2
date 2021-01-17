import csv
import torch
from torch import nn, optim 
from torch.utils.data import Dataset, DataLoader

from make_dictionary import build_dictionary


def load_data(word2token):
    # tsv読み込み
    with open('data/total.csv')as f:
        reader = csv.reader(f, delimiter=',')
        label_data = []
        input_data = []
        for i, row in enumerate(reader):
            if i == 0:
                continue
            
            # ラベル付与
            if row[0] == '၌':
                label = 0
            elif row[0] == 'မှာ':
                label = 1
            elif row[0] == 'တွင်':
                label = 2
            label_data.append(label)

            # 共起する名詞
            if row[1] in word2token:
                noun = word2token[row[1]]
            else:
                noun = 0

            # 共起する動詞
            if row[2] in word2token:
                verb = word2token[row[2]]
            else:
                verb = 0

            # 共起カウント
            cnt = int(row[3])
            input_data.append([noun, verb, cnt])
            # tensorでまとめる
            
        label_data = torch.tensor(label_data).long()
        input_data = torch.tensor(input_data).float()

    return input_data, label_data
            
class MyDataset(Dataset):
    def __init__(self, input_data, label_data):
        self.input = input_data
        self.label = label_data
        self.datanum = len(label_data)
        
    def __len__(self):
        return self.datanum
    
    def __getitem__(self, idx):
        return self.input[idx], self.label[idx]

def main():
    word2token, token2word = build_dictionary()
    input_data, label_data = load_data(word2token)
    dataset = MyDataset(input_data, label_data)

    print(set(label_data))
    
    return 0

if __name__ == '__main__':
    main()

