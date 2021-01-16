# 欠損埋め

library(tidyverse)
library(data.table)


# read data
df_sub = fread("./output/df_sub_filled.csv", sep = ",", encoding = "UTF-8", header = T)
for(i in 1:(nrow(df_sub) - 1)) {
  
  if(is.na(df_sub[i]$value_verb)){
    # count
    print(paste0("loop : ", i))
    df_sub[i]$value_verb = df_sub[i + 1]$value_verb
    df_sub[i]$tag_verb = df_sub[i + 1]$tag_verb
    df_sub[i]$order_verb = df_sub[i + 1]$order_verb
  }
}

write.table(df_sub,"./output/df_sub_filled.csv", row.names = F, col.names = T, sep = ",")