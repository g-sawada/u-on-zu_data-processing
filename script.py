import pandas as pd

# df = pd.DataFrame({
#       '名前': ["佐藤", "斎藤", "鈴木"],
#       '年齢': [24, 45, 36]
#     })
# print(df)

# df = pd.read_excel('./raw/list_of_observatories_240527DL.xlsx', sheet_name=3)
df = pd.read_excel('./raw/list_of_observatories_240527DL.xlsx', sheet_name=3)

print(df)
