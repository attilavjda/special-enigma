import matplotlib.pyplot as plt
import numpy as np

# Probability distribution
prob_dist = [0.1, 0.15, 0.2, 0.25, 0.2, 0.1]
categories = ['A', 'B', 'C', 'D', 'E', 'F']

# Pie Chart
fig, ax = plt.subplots()
ax.pie(prob_dist, labels=categories, autopct='%1.1f%%')
ax.axis('equal')
ax.set_facecolor('#141414')
ax.set_title('Pie Chart', color='#FFFFFF')

# Bar Chart
fig, ax = plt.subplots()
ax.bar(categories, prob_dist)
ax.set_facecolor('#141414')
ax.set_title('Bar Chart', color='#FFFFFF')
ax.set_xlabel('Events', color='#FFFFFF')
ax.set_ylabel('Probability', color='#FFFFFF')

# Line Chart
fig, ax = plt.subplots()
x = np.arange(len(categories))
ax.plot(x, prob_dist, color='#FFFFFF')
ax.fill_between(x, prob_dist, alpha=0.2, color='#FFFFFF')
ax.set_facecolor('#141414')
ax.set_title('Line Chart', color='#FFFFFF')
ax.set_xlabel('Events', color='#FFFFFF')
ax.set_ylabel('Probability', color='#FFFFFF')

# Area Chart
fig, ax = plt.subplots()
ax.plot(x, prob_dist, color='#FFFFFF')
ax.fill_between(x, prob_dist, alpha=0.2, color='#FFFFFF')
ax.set_facecolor('#141414')
ax.set_title('Area Chart', color='#FFFFFF')
ax.set_xlabel('Events', color='#FFFFFF')
ax.set_ylabel('Probability', color='#FFFFFF')

# Heatmap
fig, ax = plt.subplots()
ax.pcolor(prob_dist_array.reshape(1, -1), cmap='Blues', edgecolors='white')
ax.set_facecolor('#141414')
ax.set_title('Heatmap', color='#FFFFFF')
ax.set_xlabel('Events', color='#FFFFFF')
ax.set_ylabel('Probability', color='#FFFFFF')

# Violin Plot
from violinplotz import violin_plot_z

fig, ax = plt.subplots()
violin_plot_z(prob_dist, categories, ax=ax, inner='box', color='#FFFFFF', edgecolor='#FFFFFF')
ax.set_facecolor('#141414')
ax.set_title('Violin Plot', color='#FFFFFF')
ax.set_xlabel('Events', color='#FFFFFF')
ax.set_ylabel('Probability', color='#FFFFFF')

plt.show()
