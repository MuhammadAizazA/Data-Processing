import pandas as pd
path='data/excel_merge_csv_files.xlsx'
df=pd.read_excel('data/new_excel_file_2.xlsx')
excel_file=pd.ExcelFile(path)
row=pd.read_excel(path, sheet_name=0).iloc[2]['Name']
df_5=pd.read_excel(path, sheet_name=1, usecols=["Name"]).iloc[0]
print("The dataframe column is:")

print(excel_file.sheet_names)
print(df)
print(row)
print(df_5)