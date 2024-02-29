import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv', sep=';', skipinitialspace=True, encoding="cp1251")
df.columns = df.columns.str.replace(' ', '_')
df.columns = df.columns.str.lower()
column = "возраст"
df1 = df.groupby(["пол"])
print(df1.head(50))
sns.kdeplot(df1[column].get_group("муж"), fill=True, legend=True)
sns.kdeplot(df1[column].get_group("жен"), fill=True, legend=True)
plt.xlabel(column)
plt.show()
