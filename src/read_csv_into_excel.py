import pandas as pd

df=pd.read_csv('data/height_file.csv')

with pd.ExcelWriter('data/csv_into_excel_1.xlsx',engine='openpyxl') as writer:
    df.to_excel(writer,index=True,startcol=1,startrow=1,index_label="S.No")