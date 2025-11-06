import pandas as pd

df = pd.read_excel("overtime.xlsx", engine="openpyxl")

print(df)
print("总加班时长：", df["Hours"].sum(), "小时")

