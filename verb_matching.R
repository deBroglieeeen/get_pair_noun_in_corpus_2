# マッチング

library(tidyverse)
library(data.table)

rm(list = ls())

# read data
df_sample = fread("./output/df_sample_verb.tsv", sep = "\t", encoding = "UTF-8", header = T)

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

check = FALSE
for (i in 1:nrow(df_output)) {
  # count
  print(paste0("loop : ", i))
  #if (df_output$tag[i] == "noun") {
  #if (df_output$tag[i] == "verb") {
  #  tag_tmp = df_output$tag[i]
  #  value_tmp = df_output$value[i]
  #  order_tmp = df_output$order[i]
  #}
  
  if (df_output$tar_flg[i] == 1) {
    check = TRUE
    tar_index = i
    #tag_target = df_output$tag[i]
    #value_target = df_output$value[i]
    #order_tmp = df_output$order[i]
  }
  if(check == TRUE && df_output$tag[i] == "verb") {
    df_output$tag_pair[tar_index] = df_output$tag[i]
    df_output$value_pair[tar_index] = df_output$value[i]
    df_output$order_pair[tar_index] = df_output$order[i]
    check = FALSE
  }
}

# 全データOutput
write.table(df_output, "./output/df_output_verb.tsv", row.names = F, col.names = T, sep = "\t")

# TargetデータOutput
#df_output %>%
 # filter(tar_flg == 1) %>%
  #write.table("./output/df_sub.tsv", row.names = F, col.names = T, sep = "\t")

df_sub = df_output %>%
  filter(tar_flg == 1)
