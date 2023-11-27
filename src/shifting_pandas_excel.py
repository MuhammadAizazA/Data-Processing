import pandas as pd

data=[["Aditya",179],
      ["Sameer",181],
      ["Dharwish",170],
      ["Joel",167]]

column_names=["Name", "Height"]

df=pd.DataFrame(data, columns=column_names)

writer = pd.ExcelWriter('data/excel_with_list_displaced.xlsx', engine='openpyxl')
df.to_excel(writer, sheet_name='first_sheet',index=False,startrow=3,startcol=4)
df.to_excel(writer, sheet_name='second_sheet',index=True,startrow=2,startcol=2)
writer.close()