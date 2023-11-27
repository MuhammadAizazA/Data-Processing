import pandas as pd
pd.set_option('display.max_rows', None)
df = pd.read_excel('data\Employees.xlsx')
keys=['First name','Gender','Department','ID']
new_row = [{keys[0]: 'Ali', keys[1]: 'Male', keys[2]: 1,keys[3]:len(df)+1},
           {keys[0]: 'Imran', keys[1]: 'Male', keys[2]: 1,keys[3]:len(df)+2},
           {keys[0]: 'Zain', keys[1]: 'Male', keys[2]: 1,keys[3]:len(df)+3},
           {keys[0]: 'Basit', keys[1]: 'Male', keys[2]: 1,keys[3]:len(df)+4}  
           ]
df_new=pd.DataFrame(new_row)
index_to_insert = 99

df=pd.concat([df.loc[:index_to_insert-1],df_new,df.loc[index_to_insert:]]).reset_index(drop=True)

df=df.sort_values(by='ID').reset_index(drop=True)

with pd.ExcelWriter("src/employees-op/gamma_Employees.xlsx",mode='w',engine='openpyxl') as writter:
    df.to_excel(writter)

