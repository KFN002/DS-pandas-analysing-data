import pandas as pd

df = pd.read_csv('data_old.csv', sep=',', skipinitialspace=True)
df.columns = df.columns.str.replace(' ', '_')
df.columns = df.columns.str.lower()
df["расстояние_кат"] = \
    df["расстояние"].apply(lambda x: "домашний_регион" if x <= 300 else ("недалеко_отдома" if 300 < x <= 700 else
                                                                         "дальнее_путешествие"))


df = df.groupby(["расстояние_кат", "путешествует_с_детьми"])
df = pd.DataFrame(round(df["общая_оценка_качества_предоставленной_услуги"].
                        value_counts(normalize=True)['плохо'].mul(100), 1).astype(float))
df.columns = ["0"]
df = df.sort_index()
print(df)
