import pandas as pd
import scipy as sp
import scipy.stats

# コンマ区切りのテキストデータを読み込む
data = pd.read_csv("output/df_sub_sum_verb.csv", sep=",")

# print(data.value)
# print(data.head())
hnai = data[data["value"] == "၌"]
dwin = data[data["value"] == "တွင်"]
hma = data[data["value"] == "မှာ"]
hnai.to_csv('output/hnai_verb.csv')
dwin.to_csv('output/dwin_verb.csv')
hma.to_csv('output/hma_verb.csv')
hnai.head(15).to_csv('output/hnai_verb_head.csv')
dwin.head(15).to_csv('output/dwin_verb_head.csv')
hma.head(15).to_csv('output/hma_verb_head.csv')
marged = pd.concat([hnai,dwin,hma],axis = 0)
pivot_verb = pd.pivot_table(marged, index = "value_pair",columns = "value")
#pivot_verb = pivot_verb.sort_values(["တွင်","၌"],axis=0, ascending = (False,True) )

pivot_verb.to_csv('output/pivot_verb.csv')
# print(dwin.head())
# print(hma.head())
#table = data.loc[data["value"] == "၌" | data["value"] == "တွင်",data["value_pair"] == "မြို့" | data["value_pair"] == "ဆေးရုံ" ]

# ၌ တွင်のみを抽出
HD = data[(data["value"] == "၌") | (data["value"] == "တွင်")]
