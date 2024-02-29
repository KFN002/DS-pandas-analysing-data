import pandas as pd


data = pd.read_csv('cake_5.csv', sep=',', encoding='cp1251')
z = 1.96
data = data[data["вес_шоколадки"] >= 100]
sample_std = data['вес_шоколадки'].std()
sample_size = len(data)
margin_error = (z * sample_std) / (sample_size ** 0.5)
margin_error2 = margin_error / 5
sample_size2 = ((z * sample_std) / margin_error2) ** 2
print(f"{round(margin_error, 3)} , {round(sample_size2)}")

'''
0.083 , 4897
'''
