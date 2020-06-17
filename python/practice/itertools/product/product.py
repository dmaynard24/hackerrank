import itertools


def product(a, b):
  return ' '.join(map(str, list(itertools.product(a, b))))