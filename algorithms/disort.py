from typing import Iterable, TypeVar, MutableSequence

def disort(data: MutableSequence) -> MutableSequence:
    """ Insertion sort elements in descending order. """
    for j in range(1, len(A)):
        k, i = data[j], j - 1
        while i >= 0 and data[i] < k:
            data[i + 1] = data[i]
            i -= 1
        data[i + 1] = k
    return data

# example usage with list
A = [31, 41, 59, 26, 41, 58]
print(disort(A))

# example usage with dictionary
d = {'a': 1, 'b': 2, 'c': 3}
print(disort(d))

# example usage with string
s = 'hello'
print(disort(s))

# example usage with tuple
t = (1, 2, 3)
print(disort(t))

# example usage with set
s = {1, 2, 3}
print(disort(s))
