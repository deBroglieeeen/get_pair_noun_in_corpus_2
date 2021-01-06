# Visualize例

# TargetデータOutput


df_sub_sum = df_sub %>%
  mutate(count = 1) %>%
  group_by(value, value_pair) %>%
  summarise_at(vars(count), funs(sum)) %>%
  arrange(value, desc(count))

write.table(df_sub_sum, "./output/df_sub_sum2.csv", row.names = F, col.names = T, sep = ",")
