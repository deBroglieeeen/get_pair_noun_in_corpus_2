# Visualize例

# TargetデータOutput


df_sub_sum = df_sub %>%
  mutate(count = 1) %>%
  group_by(value, value_noun, value_verb) %>%
  summarise_at(vars(count), funs(sum)) %>%
  arrange(value, desc(count))

write.table(df_sub_sum, "./output/df_sub_sum_analize.csv", row.names = F, col.names = T, sep = ",")

