import csv

def build_dictionary():
    # tsv読み込み
    with open('../output/df_output_analize.tsv')as f:
        tsv_reader = csv.reader(f, delimiter='\t')
        read_data = [row[2] for row in tsv_reader]

    # 名詞と動詞のみの辞書作成
    word2token = {}
    token2word = {}
    # トークン初期値
    token = 1
    for word in read_data:
        if word in word2token:
            continue
        else:
            word2token[word] = token
            token2word[token] = word
            token += 1

    return word2token, token2word

def main():
    word2token, token2word = build_dictionary()

if __name__ == '__main__':
    main()