import os
import pandas as pd

file_path = os.path.join('data', 'new_excel_file_2.xlsx')

try:
    # Append to an existing Excel file or create a new one if it doesn't exist
    writer = pd.ExcelWriter(file_path,mode='a',engine="openpyxl",if_sheet_exists="replace")
    df=pd.read_excel(file_path, sheet_name='user_details')
    newRow= {"Name":"Alon","Marks":77}
    new_row=pd.DataFrame([newRow])
    df=pd.concat([df,new_row],ignore_index=True)

    # Write the pandas dataframe to the excel file
    df.to_excel(writer, sheet_name="user_details",index=False)
    writer.close()

except PermissionError as e:
    print(f"PermissionError: {e}")
    print("Please check file path and permissions.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")