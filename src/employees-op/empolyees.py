import pandas as pd

# Assuming you've already read the Excel file and stored it in the 'df' variable
df = pd.read_excel('D:\Repo\Data-Processing\data\Employees.xlsx', sheet_name=0)

# Set the display option to show all rows
pd.set_option('display.max_rows', None)

# Print the entire DataFrame
print("Original DataFrame:")
print(df)

# Initialize an empty list to store filtered DataFrames
filtered_df_list = []

# Filter the DataFrame based on the first character of 'First name' for each letter of the alphabet
for start in range(26):
    x = 'A'
    alphabet = chr(ord(x) + start)
    filtered_df = df[df['First name'].str[0] == alphabet]
    filtered_df_list.append(filtered_df)

    # Save the filtered DataFrame to a separate sheet in the Excel file
    with pd.ExcelWriter("src/employees-op/Alpha_Employees.xlsx", mode="a", engine='openpyxl',if_sheet_exists='replace') as writer:
        filtered_df.to_excel(writer, sheet_name=f"Sheet No {start}", index=False)

# Print the filtered DataFrames for each letter of the alphabet
print("\nFiltered DataFrames:")
for index, df in enumerate(filtered_df_list):
    print(f"\nDataFrame for '{chr(ord('A') + index)}':")
    print(df)
