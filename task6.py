import pandas
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv", sep=',')
data.columns = data.columns.str.lower().str.replace(' ', '_')


def plot_histogram_and_boxplot(category):
    fig, axes = plt.subplots(1, 2, figsize=(9, 3))
    selected_data = data[data['покупательская_активность'] == category]
    print(selected_data["выручка_от_клиента_текущий_месяц"])
    g1 = sns.histplot(pandas.DataFrame(selected_data["выручка_от_клиента_текущий_месяц"]),
                      bins=30, kde=True, ax=axes[0], legend=False)
    g1.set(ylabel=None)
    g2 = sns.boxplot(y=selected_data["выручка_от_клиента_текущий_месяц"], ax=axes[1])
    g2.set(ylabel=None, xlabel=0)
    fig.suptitle('Гистограмма и ящик с усами для количественных данных')
    plt.savefig('target_4_6.png')
    plt.show()


plot_histogram_and_boxplot(input())
