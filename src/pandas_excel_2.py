import os
import pandas as pd

data = [["Aditya", 179],
        ["Sameer", 181],
        ["Dharwesh", 170],
        ["Joel", 167]]

row_name = ['first', 'second', 'third']
columns_name = ['Name', 'Marks']

df = pd.DataFrame(data, columns=columns_name)

file_path = os.path.join('data', 'new_excel_file_2.xlsx')

try:
    # Append to an existing Excel file or create a new one if it doesn't exist
    with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='user_details', index=True,startcol=3)
        df.to_excel(writer, sheet_name='first_sheet', index=False,startcol=3)

except PermissionError as e:
    print(f"PermissionError: {e}")
    print("Please check file path and permissions.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
