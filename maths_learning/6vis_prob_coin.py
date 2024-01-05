import matplotlib.pyplot as plt
import numpy as np

# Function to simulate coin tosses and calculate probabilities
def simulate_coin_tosses(num_trials):
    outcomes = np.random.choice(['H', 'T'], num_trials)
    unique, counts = np.unique(outcomes, return_counts=True)
    probabilities = counts / num_trials
    return unique, probabilities

# Number of trials
num_trials = 1000

# Visualization 1: Bar chart of outcomes
outcomes, probabilities = simulate_coin_tosses(num_trials)
plt.subplot(2, 3, 1)
plt.bar(outcomes, probabilities)
plt.title('Outcome Frequencies')

# Visualization 2: Pie chart of outcomes
plt.subplot(2, 3, 2)
plt.pie(probabilities, labels=outcomes, autopct='%1.1f%%')
plt.title('Outcome Proportions')

# Visualization 3: Line chart of cumulative probabilities
cumulative_probabilities = np.cumsum(probabilities)
plt.subplot(2, 3, 3)
plt.plot(outcomes, cumulative_probabilities, marker='o')
plt.title('Cumulative Probabilities')

# Visualization 4: Histogram of simulated coin tosses
plt.subplot(2, 3, 4)
plt.hist(np.random.choice([0, 1], size=num_trials, p=probabilities), bins=[-0.5, 0.5, 1.5], align='mid', rwidth=0.8)
plt.xticks([0, 1], ['H', 'T'])
plt.title('Simulated Coin Tosses')

# Visualization 5: Box plot of simulated coin tosses
plt.subplot(2, 3, 5)
plt.boxplot(np.random.choice([0, 1], size=num_trials, p=probabilities), vert=False)
plt.yticks([1], ['Coin Tosses'])
plt.title('Box Plot of Tosses')

# Visualization 6: Heatmap of joint probabilities
joint_probabilities = np.outer(probabilities, probabilities)
plt.subplot(2, 3, 6)
plt.imshow(joint_probabilities, cmap='Blues', interpolation='nearest')
plt.colorbar()
plt.title('Joint Probabilities')

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()
