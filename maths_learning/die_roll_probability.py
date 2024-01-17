# roll a die 10 times
# store k, k/n, P(A)
# plot k/n vs P(A)

import random


def roll_die():
    return random.randint(1, 6)


def main():
    k = 0
    n = 10
    for i in range(n):
        k += roll_die()
    print(k)
    print(k / n)
    print(1 / 6)
    print(k / n / 6)



    


