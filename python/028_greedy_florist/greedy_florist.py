import math


def getMinimumCost(k, c):
  c.sort(reverse=True)

  cost = 0
  for i in range(len(c)):
    cost += c[i] * math.ceil((i + 1) / k)

  return cost


print(getMinimumCost(2, [2, 5, 6]))  # 15
print(getMinimumCost(3, [1, 3, 5, 7, 9]))  # 29
