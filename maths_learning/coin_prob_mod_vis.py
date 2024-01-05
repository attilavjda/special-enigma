import matplotlib.pyplot as plt

plt.style.use('dark_background')

probabilities = [0.5, 0.5]
categories = ['Heads', 'Tails']

plt.bar(categories, probabilities)
plt.xlabel('Outcome')
plt.ylabel('Probability')
plt.title('Probability Model for Coin Toss')
plt.show()