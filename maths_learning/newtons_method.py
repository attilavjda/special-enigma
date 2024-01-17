from math import log

def f(x):
  return 3**x + 3**(3*x) - 10

def f_prime(x):
  return 3**x * log(3) + 9 * 3**(3*x) * log(3)

def newton(x, tol=1e-6):
  while abs(f(x)) > tol:
    x = x - f(x) / f_prime(x)
  return x

x = newton(0.5)
print(f"The solution is approximately {x}")
