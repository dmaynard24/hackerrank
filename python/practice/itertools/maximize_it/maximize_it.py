from itertools import product


def maximize_it(k, m, x):
  products = list(product(*x))
  return max(sum([n**2 for n in p]) % m for p in products)