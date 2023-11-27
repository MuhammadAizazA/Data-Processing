import pandas as pd

pd.set_option('display.max_rows', None)

# Assuming you have an existing DataFrame df
df = pd.read_excel('data\Employees.xlsx')
# Create new rows as dictionaries with incremented 'ID'
new_row = [
    {'First name': 'John', 'Gender': 'Male', 'Department': 1, 'ID': df['ID'].max() + 1},
    {'First name': 'Aizaz', 'Gender': 'Male', 'Department': 5, 'ID': df['ID'].max() + 2}
]

# Create a new DataFrame with the new rows
new_pd = pd.DataFrame(new_row)

# Append the new rows to the existing DataFrame
df = pd.concat([df, new_pd], ignore_index=True)
with pd.ExcelWriter('data\Employees.xlsx',mode='a',engine='openpyxl',if_sheet_exists='replace') as writter:
    df.to_excel(writter)
# Print the DataFrame with the new rows
print("\nDataFrame after adding new rows:")
print(df)
