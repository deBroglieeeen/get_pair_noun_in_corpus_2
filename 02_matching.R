# マッチング

library(tidyverse)
library(data.table)

rm(list = ls())

# read data
rawdata = fread("./output/df_sample.tsv", sep = "\t", encoding = "UTF-8", header = T) 

# 追加加工
df_output = df_sample %>% 
  mutate(tar_flg = ifelse(tag == "adp" & value == "တွင်" |
                          tag == "adp" & value == "မှာ"|
                          tag == "adp" & value == "၌", 1, 0)) %>% 
  mutate(tag_pair = NA) %>% 
  mutate(value_pair = NA) %>% 
  mutate(order_pair = NA)

for (i in 1:nrow(df_output)) {
  if (df_output$tag[i] == "noun") {
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
write.table(df_output, "./output/df_output.tsv", col.names = F, sep = "\t")

# TargetデータOutput
df_output %>%
  filter(tar_flg == 1) %>% 
  write.table("./output/df_sub.tsv", col.names = F, sep = "\t")
