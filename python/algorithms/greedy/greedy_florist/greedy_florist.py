import math


def get_minimum_cost(k, c):
  c.sort(reverse=True)

  cost = 0
  for i in range(len(c)):
    cost += c[i] * math.ceil((i + 1) / k)

  return cost
