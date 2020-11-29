'''Create a scatter plot showing the relationship between the total revenue earned by arcades and the number of Computer Science PhDs awarded in the U.S. between 2000 and 2009.
Don't forget to label your axes!
Color each dot according to its year.'''


# Import Libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.cm as cm


# Step 2. Import the dataset from this address
arcade_revenue_cs_doctorates = pd.read_csv('arcade-revenue-vs-cs-doctorates.csv')
size = np.arange(len(arcade_revenue_cs_doctorates.Year))

# Plot
colors = cm.rainbow(np.linspace(0, 5, len(size)))
plt.scatter(arcade_revenue_cs_doctorates.Total_Arcade_Revenue_billions, arcade_revenue_cs_doctorates.Computer_Science_Doctorates_Awarded_US, s=size)
plt.title('scatter plot')
plt.show()