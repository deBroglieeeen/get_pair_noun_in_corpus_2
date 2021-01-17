import pandas as pd
import scipy as sp
import scipy.stats

# コンマ区切りのテキストデータを読み込む
data = pd.read_csv("output/df_sample2.tsv", sep='/t')

data.head(15).to_csv('output/head_alldata_sample.csv')
