import pandas as pd

df=pd.read_excel('data/new_excel_file_2.xlsx')
excel_file=pd.ExcelFile('data/excel_merge_csv_files.xlsx')
row=pd.read_excel('data/excel_merge_csv_files.xlsx', sheet_name=0).iloc[2]
print(excel_file.sheet_names)
print(df)
print(row)