import csv
import torch
from torch import nn, optim 
from torch.utils.data import Dataset, DataLoader

from make_dictionary import build_dictionary


def load_data(word2token):
    # tsv読み込み
    with open('data/total.csv')as f:
        reader = csv.reader(f, delimiter=',')
        output_data = []
        noun_data = []
        verb_data = []
        cnt_data = []
        for i, row in enumerate(reader):
            if i == 0:
                continue

            if row[0] in word2token:
                output = word2token[row[0]]
            else:
                output = 0
            output_data.append(output)

            if row[1] in word2token:
                noun = word2token[row[1]]
            else:
                noun = 0
            noun_data.append(noun)

            if row[2] in word2token:
                verb = word2token[row[2]]
            else:
                verb = 0
            verb_data.append(verb)

            cnt = int(row[3])
            cnt_data.append(cnt)
            # tensorでまとめる
            
        output_data = torch.tensor(output_data)
        noun_data = torch.tensor(noun_data)
        verb_data = torch.tensor(verb_data)
        cnt_data = torch.tensor(cnt_data)
    return output_data, noun_data, verb_data, cnt_data
            
class MyDataset(Dataset):
    def __init__(self, output_data, noun_data, verb_data, cnt_data):
        self.output = output_data
        self.noun = noun_data
        self.verb = verb_data
        self.cnt = cnt_data
        self.datanum = len(output_data)
        
    def __len__(self):
        return self.datanum
    
    def __getitem__(self, idx):
        return self.noun[idx], self.verb[idx], self.cnt[idx], self.output[idx]

def main():
    word2token, token2word = build_dictionary()
    output_data, noun_data, verb_data, cnt_data = load_data(word2token)
    dataset = MyDataset(output_data, noun_data, verb_data, cnt_data)
    
    return 0

if __name__ == '__main__':
    main()

