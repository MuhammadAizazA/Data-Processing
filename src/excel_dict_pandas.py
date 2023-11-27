import pandas as pd

names=[{'name':'Aizaz','Age':20},{'name':'Bilal','Age':20},{'name':'Camran','Age':20}]
df=pd.DataFrame(names)
with pd.ExcelWriter('data/new_excel_file_3.xlsx',engine='xlsxwriter') as writter:
    df.to_excel(writter,sheet_name='practice_dictionary',index=False)