import pandas as pd

df = pd.read_csv('data.csv', sep=',', skipinitialspace=True)
df.columns = df.columns.str.replace(' ', '_')
df.columns = df.columns.str.lower()
category1 = ["Домашний текстиль",
             "Кухонная посуда",
             "Мелкая бытовая техника и электроника"]
df["категории_товаров"] = df["популярная_категория"] \
    .apply(lambda x: "покупки для быта" if x in category1 else "покупки для себя")
new_data = df.query('категории_товаров == "покупки для быта"')
new_data = new_data.groupby(["покупательская_активность"])
described = pd.DataFrame(new_data["разность_выручки_тек_прошлый_месяц"].describe().T)
described = described.astype(int).T
print(described)
