import pandas as pd
import scipy as sp
from scipy import stats

# 表示桁数の指定
#%precision 3

# コンマ区切りのテキストデータを読み込む
noun_data = pd.read_csv("output/df_sub_sum2.csv", sep=",")
verb_data = pd.read_csv("output/df_sub_sum_verb.csv", sep=",")

# hnai-noun = noun_data[noun_data["value"] == "၌"]
# dwin_noun = noun_data[noun_data["value"] == "တွင်"]
# hma_noun = noun_data[noun_data["value"] == "မှာ"]
# hnai_verb = verb_data[verb_data["value"] == "၌"]
# dwin_verb = verb_data[verb_data["value"] == "တွင်"]
# hma_verb = verb_data[verb_data["value"] == "မှာ"]
# print(hnai_verb["value_pair"] == "မြို့")
# # ၌ တွင်のみを抽出
# HD = noun_data[(noun_data["value"] == "၌") | (noun_data["value"] == "တွင်")]

# hnai-nounDwinMyoSeyoun = HD[(HD["value_pair"] == "မြို့") | (HD["value_pair"] == "ဆေးရုံ")]
# print(hnai-nounDwinMyoSeyoun)
# hnai-nounMyoSeyoun = hnai-noun[(hnai-noun["value_pair"] == "မြို့") | (hnai-noun["value_pair"] == "ဆေးရုံ")]
# dwin_nounMyoSeyoun = dwin_noun[(dwin_noun["value_pair"] == "မြို့") | (dwin_noun["value_pair"] == "ဆေးရုံ")]


# crosstab = pd.crosstab(hnai-nounDwinMyoSeyoun["value"],hnai-nounDwinMyoSeyoun["count"])
# print(crosstab)
# print(pd.pivot_table(hnai-nounDwinMyoSeyoun, index="value",columns="value_pair"))
noun_head = pd.read_csv("output/位置の補語　共起頻度 - noun_merged (3).csv", sep=",")
verb_head = pd.read_csv("output/動詞　位置の補語　共起頻度 - merged_head_verb (1).csv", sep=",")
def burmese_chisq_test(data):
    value = []
    x2 = []
    p = []
    dof = []
    significant = []
    for row in data.itertuples():
        #a = input()
        print(type(row))
        print(row)
        a = row.value
        dwin_other = 9882 - row.dwin
        hnai_other = 1137 - row.hnai
        print(dwin_other)
        print(hnai_other)
        print(a)
        test_data = pd.DataFrame({"adposition":["တွင်","တွင်","၌","၌"], "co-occurrence":[a, "other", a, "other"], "number":[row.dwin, dwin_other, row.hnai, hnai_other]})
        cross_data = pd.pivot_table(data = test_data, values = "number", aggfunc = "sum",index = "adposition", columns = "co-occurrence")
        b, c, d, expected = sp.stats.chi2_contingency(cross_data)
        value.append(a)
        x2.append(b)
        p.append(c)
        dof.append(d)
        if c < 0.05:
            significant.append(1)
        else:
            significant.append(0)
        print(expected)
    return pd.DataFrame({"value":value, "x2":x2, "p":p, "dof":dof, "significant":significant})
burmese_chisq_test(noun_head).to_csv("output/chisq_noun_head.csv")
burmese_chisq_test(verb_head).to_csv("output/chisq_verb_head.csv")
# pivot = pd.pivot_table(hnai-nounDwinMyoSeyoun, index="value", columns="value_pair")

# x2, p, dof, expected = sp.stats.chi2_contingency(pivot)

# print("カイ二乗値は %(x2)s" %locals() )
# print("確率は %(p)s" %locals() )
# print("自由度は %(dof)s" %locals() )
# print( expected )

# if p < 0.05:
#     print("有意な差があります")
# else:
#     print("有意な差がありません")

# print(x2)
