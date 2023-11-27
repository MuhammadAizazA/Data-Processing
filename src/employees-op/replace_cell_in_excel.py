import pandas as pd

pd.set_option('display.max_rows', None)

# Assuming you have an existing DataFrame df
df = pd.read_excel('data\Employees.xlsx')

# Print the original DataFrame
print("Original DataFrame:")
name='Ali'
df.loc[10, 'First name']=name
with pd.ExcelWriter("src/employees-op/Beta_Employees.xlsx",mode='w',engine='openpyxl') as writter:
    df.to_excel(writter,index=True)
print(df.loc[10])
name='Jahangir'
df.loc[11, 'First name']=name
with pd.ExcelWriter("src/employees-op/Beta_Employees.xlsx",mode='w',engine='openpyxl') as writter:
    df.to_excel(writter,index=True)