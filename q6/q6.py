'''Create a line plot showing the number of marriages and divorces per capita in the U.S. between 1867 and 2014. Label both lines and show the legend.
Don't forget to label your axes!'''


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


us_marriage_divorce_data = pd.read_csv('us-marriages-divorces-1867-2014.csv')
plt.figure(figsize=(8,5))
plt.title('Us marriage divorce data', fontdict={'fontweight':'bold', 'fontsize': 12})
plt.plot(us_marriage_divorce_data.Year, us_marriage_divorce_data.Marriages, 'b.-', label='Marriages')
plt.plot(us_marriage_divorce_data.Year, us_marriage_divorce_data.Divorces, 'r.-', label='Divorces')
plt.xlabel('Year')
plt.ylabel('Marriages\Divorces per capita')
plt.legend()
plt.savefig('Us marriage divorce data.png', dpi=300)
plt.show()