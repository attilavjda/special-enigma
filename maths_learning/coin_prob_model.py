import random

num_trials = 1000000
num_heads = 0

for i in range(num_trials):
    coin_toss = random.choice(['H', 'T'])
    if coin_toss == 'H':
        num_heads += 1

probability_heads = num_heads / num_trials
print(probability_heads)