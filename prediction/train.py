import csv
import torch
from torch import nn, optim 
from torch.utils.data import Dataset, DataLoader, random_split

from make_dictionary import build_dictionary
from dataset import MyDataset, load_data

def main():
    word2token, token2word = build_dictionary()
    output_data, noun_data, verb_data, cnt_data = load_data(word2token)
    dataset = MyDataset(output_data, noun_data, verb_data, cnt_data)
    n_samples = len(dataset)
    val_size = n_samples*0.1
    train_size = n_samples - val_size
    train_dataset, val_dataset = random_split(dataset, [train_size, val_size])
    train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=32, shuffle=True)

    
    

    return 0


if __name__ == '__main__':
    main()