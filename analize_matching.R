# マッチング

library(tidyverse)
library(data.table)

rm(list = ls())

# read data
df_sample = fread("./output/df_sample_analize.tsv", sep = "\t", encoding = "UTF-8", header = T)

# 追加加工
df_output = df_sample %>%
  mutate(tar_flg = ifelse(tag == "adp" & value == "တွင်" |
                          tag == "adp" & value == "မှာ"|
                          tag == "adp" & value == "၌", 1, 0)) %>%
  mutate(tag_noun = NA) %>%
  mutate(value_noun = NA) %>%
  mutate(order_noun = NA) %>%
  mutate(tag_verb = NA) %>%
  mutate(value_verb = NA) %>%
  mutate(order_verb = NA)

check = FALSE
for (i in 1:nrow(df_output)) {
  # count
  print(paste0("loop : ", i))
  if(check == FALSE && df_output$tag[i] == "noun") {
    tag_tmp = df_output$tag[i]
    value_tmp = df_output$value[i]
    order_tmp = df_output$order[i]
  }
  
  if (df_output$tar_flg[i] == 1) {
    check = TRUE
    tar_index = i
    df_output$tag_noun[i] = tag_tmp
    df_output$value_noun[i] = value_tmp
    df_output$order_noun[i] = order_tmp
  }
  if(check == TRUE && df_output$tag[i] == "verb") {
    df_output$tag_verb[tar_index] = df_output$tag[i]
    df_output$value_verb[tar_index] = df_output$value[i]
    df_output$order_verb[tar_index] = df_output$order[i]
    check = FALSE
  }
}

# 全データOutput
write.table(df_output, "./output/df_output_analize.tsv", row.names = F, col.names = T, sep = "\t")

# TargetデータOutput
#df_output %>%
 # filter(tar_flg == 1) %>%
  #write.table("./output/df_sub.tsv", row.names = F, col.names = T, sep = "\t")

df_sub = df_output %>%
  filter(tar_flg == 1)
