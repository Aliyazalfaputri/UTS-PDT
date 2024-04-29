import pandas as pd

df_xlsx = pd.read_excel('water_potability.xlsx')
df_txt = pd.read_csv('water_potability.txt')

# For TXT file
print("TXT Data Summary:")
print("Count Rows:", len(df_txt))
print("Mean:")
print(df_txt.mean())
print("Median:")
print(df_txt.median())
print()

# For XLSX file
print("XLSX Data Summary:")
print("Count Rows:", len(df_xlsx))
print("Mean:")
print(df_xlsx.mean())
print("Median:")
print(df_xlsx.median())
