import pandas as pd

data = [["Aditya", 179],
        ["Sameer", 181],
        ["Dharwish", 170],
        ["Joel", 167]]

row_name = ['first', 'second', 'third']
columns_name = ['Name', 'Marks']

df = pd.DataFrame(data, columns=columns_name)

# Append to an existing Excel file or create a new one if it doesn't exist
with pd.ExcelWriter('data/new_excel_file_4.xlsx', engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='user_details', index=False,startcol=3)
    df.to_excel(writer, sheet_name='first_sheet', index=False)
