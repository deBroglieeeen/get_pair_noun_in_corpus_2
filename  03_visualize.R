# Visualize例

df_sub_sum = df_sub %>% 
  mutate(count = 1) %>% 
  group_by(value, value_pair) %>% 
  summarise_at(vars(count), funs(sum)) %>% 
  arrange(value, desc(count))
