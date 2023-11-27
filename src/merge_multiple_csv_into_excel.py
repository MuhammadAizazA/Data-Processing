import pandas as pd

df_height=pd.read_csv("data/height_file.csv")
df_marks=pd.read_csv("data/marks_file.csv")
df_weight=pd.read_csv("data/weight_file.csv")

writer = pd.ExcelWriter('data/excel_merge_csv_files.xlsx', engine='openpyxl')

df_height.to_excel(writer, sheet_name='height',index=False)
df_marks.to_excel(writer, sheet_name='marks',index=False)
df_weight.to_excel(writer, sheet_name='weight',index=False)

writer.close()