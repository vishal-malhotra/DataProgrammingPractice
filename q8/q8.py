'''Create a horizontal bar chart that compares the deadliest actors in Hollywood. Sort the actors by their kill count and label each bar with the corresponding actor's name.'''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



hollywood_actor_kills = pd.read_csv('actor_kill_counts.csv')
hollywood_actor_kills=hollywood_actor_kills.sort_values(by=['Count'],ascending=False)
actor_names = tuple(hollywood_actor_kills['Actor'].values.tolist())
kill_counts = hollywood_actor_kills['Count'].values.tolist()
hollywood_actor_kills
objects = actor_names
y_pos = np.arange(len(objects))
performance = kill_counts
plt.barh(y_pos, performance, align='center', alpha=0.5)
plt.yticks(y_pos, objects)
plt.xlabel('Kills')
plt.title('Deadliest actors in Hollywood')
plt.show()
