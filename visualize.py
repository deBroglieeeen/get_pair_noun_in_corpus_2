import pandas as pd
import scipy as sp
import scipy.stats

# コンマ区切りのテキストデータを読み込む
data = pd.read_csv("output/df_sub_sum2.csv", sep=",")

hnai = data[data["value"] == "၌"]
dwin = data[data["value"] == "တွင်"]
hma = data[data["value"] == "မှာ"]


hnai.to_csv('output/hnai_output.csv')
dwin.to_csv('output/dwin_output.csv')
hma.to_csv('output/hma_output.csv')
hnai.head(15).to_csv('output/hnai_output_head.csv')
dwin.head(15).to_csv('output/dwin_output_head.csv')
hma.head(15).to_csv('output/hma_output_head.csv')
# print(dwin.head())
# print(hma.head())
#table = data.loc[data["value"] == "၌" | data["value"] == "တွင်",data["value_pair"] == "မြို့" | data["value_pair"] == "ဆေးရုံ" ]

# ၌ တွင်のみを抽出
HD = data[(data["value"] == "၌") | (data["value"] == "တွင်")]
#print(HD)

hnaiDwinMyoSeyoun = HD[(HD["value_pair"] == "မြို့") | (HD["value_pair"] == "ဆေးရုံ")]
print(hnaiDwinMyoSeyoun)
hnaiMyoSeyoun = hnai[(hnai["value_pair"] == "မြို့") | (hnai["value_pair"] == "ဆေးရုံ")]
dwinMyoSeyoun = dwin[(dwin["value_pair"] == "မြို့") | (dwin["value_pair"] == "ဆေးရုံ")]

#print(hnaiMyoSeyoun)
#print(dwinMyoSeyoun)
#crosstab = pd.crosstab(hnaiDwinMyoSeyoun)

crosstab = pd.crosstab(hnaiDwinMyoSeyoun["value"],hnaiDwinMyoSeyoun["count"])
print(crosstab)
print(pd.pivot_table(hnaiDwinMyoSeyoun, index="value",columns="value_pair"))
pivot = pd.pivot_table(hnaiDwinMyoSeyoun, index="value",columns="value_pair")
#print(pd.crosstab())

x2, p, dof, expected = sp.stats.chi2_contingency(pivot)

print("カイ二乗値は %(x2)s" %locals() )
print("確率は %(p)s" %locals() )
print("自由度は %(dof)s" %locals() )
print( expected )

if p < 0.05:
    print("有意な差があります")
else:
    print("有意な差がありません")

print(x2)
