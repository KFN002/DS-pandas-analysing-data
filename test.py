import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv', sep=',', skipinitialspace=True)
df.columns = df.columns.str.replace(' ', '_')
df.columns = df.columns.str.lower()
column = input().lower().replace(' ', '_')
df[column].value_counts().plot(kind='pie', autopct='%1.1f%%', legend=False)
plt.ylabel('')
plt.savefig('target_2_5.png')