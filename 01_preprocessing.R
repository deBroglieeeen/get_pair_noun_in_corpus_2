# Create a df_sample

library(tidyverse)
library(data.table)

rm(list = ls())

# define path
data_path = "data.txt"

# read data
rawdata = fread(data_path, sep = "\t", encoding = "UTF-8", header = F) 
colnames(rawdata) = c("V1", "V2") 

# 各種定義
ls_tag = c("adj", 
           "adp",
           "adv",
           "conj",
           "det",
           "noun",
           "noun-adp",
           "num",
           "part",
           "pron",
           "pron-adp",
           "punct",
           "verb",
           "x")

ls_tag = paste0(ls_tag, collapse = "|")

# リスト初期化
df_sample = list()

for (j in 1:nrow(rawdata)) {
  
  # count
  print(paste0("loop : ", j))
  
  # 生テキストからラフに抽出
  ls = str_extract_all(rawdata$V2[j],
                             pattern = paste0("(?<=\\()(", ls_tag, ").*?(?=\\))"), 
                             simplify = T)
  
  # "("の重複を削除
  ls_2 = str_replace_all(ls, pattern = ".+?\\s\\((.+)", replace = "\\1")
  
  # データフレームの作成
  df_tmp = data.frame(raw = ls_2, tag = NA, value = NA)
  
  # 抽出したテキストを分けてリスト化
  df_tmp = df_tmp %>% 
    mutate(tag = str_replace_all(.$raw, pattern = "(.+?)\\s.+", replacement = "\\1")) %>% 
    mutate(value = str_replace_all(.$raw, pattern = ".+?\\s(.+)", replacement = "\\1")) %>% 
    mutate(order = row_number()) %>% 
    mutate(text = rawdata$V1[j]) %>% 
    select(text, tag, value, order)
  
  df_sample = df_sample %>% bind_rows(df_tmp)
}

write.table(df_sample, "./output/df_sample.tsv", row.names = F, col.names = T, sep = "\t")

