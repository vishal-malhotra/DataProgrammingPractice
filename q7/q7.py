'''Create a vertical bar chart comparing the number of marriages and divorces per capita in the U.S. between 1900, 1950, and 2000.
Don't forget to label your axes!'''



import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

us_marriage_divorce_data = pd.read_csv('us-marriages-divorces-1867-2014.csv')
us_marriage_divorce_data = us_marriage_divorce_data[
    us_marriage_divorce_data['Year'].apply(lambda x: x in [1900, 1950, 2000])]

years = tuple(us_marriage_divorce_data['Year'].values.tolist())
marriages = tuple(us_marriage_divorce_data['Marriages'].values.tolist())
divorces= tuple(us_marriage_divorce_data['Divorces'].values.tolist())

# create plot
n_groups = 3

fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, marriages, bar_width,
alpha=opacity,
color='b',
label='Marriages')

rects2 = plt.bar(index + bar_width, divorces, bar_width,
alpha=opacity,
color='g',
label='Divorces')

plt.xlabel('Years')
plt.ylabel('Marriages\Divorces per capita')
plt.title('Us Marriage and Divorce data')
plt.xticks(index + bar_width, (1900, 1950, 2000))
plt.legend()

plt.tight_layout()
plt.show()