# マッチング

library(tidyverse)
library(data.table)

rm(list = ls())

# read data
df_sample = fread("./output/df_sample2.tsv", sep = "\t", encoding = "UTF-8", header = T)

# 追加加工
df_output = df_sample %>%
  #mutate(tar_flg = ifelse(tag == "adp" & value == "တွင်" |
  #                        tag == "adp" & value == "မှာ"|
  #                        tag == "adp" & value == "၌", 1, 0)) %>%
  mutate(tar_flg = ifelse(tag == "adp" & value == "တွင်" |
                          tag == "adp" & value == "မှာ"|
                          tag == "adp" & value == "၌", 1, 0)) %>%
  mutate(tag_pair = NA) %>%
  mutate(value_pair = NA) %>%
  mutate(order_pair = NA)

for (i in 1:nrow(df_output)) {
  # count
  print(paste0("loop : ", i))
  if (df_output$tag[i] == "noun") {
  #if (df_output$tag[i] == "verb") {
    tag_tmp = df_output$tag[i]
    value_tmp = df_output$value[i]
    order_tmp = df_output$order[i]
  }
  else if (df_output$tar_flg[i] == 1) {
    df_output$tag_pair[i] = tag_tmp
    df_output$value_pair[i] = value_tmp
    df_output$order_pair[i] = order_tmp
  }
}

# 全データOutput
write.table(df_output, "./output/df_output2.tsv", row.names = F, col.names = T, sep = "\t")

# TargetデータOutput
#df_output %>%
 # filter(tar_flg == 1) %>%
  #write.table("./output/df_sub.tsv", row.names = F, col.names = T, sep = "\t")

df_sub = df_output %>%
  filter(tar_flg == 1)
