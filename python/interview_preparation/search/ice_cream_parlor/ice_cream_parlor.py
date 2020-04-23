def ice_cream_parlor(cost, money):
  costs = {}
  for i, c in enumerate(cost):
    if money - c in costs:
      if costs[money - c] > i:
        return f'{i + 1} {costs[money-c] + 1}'
      else:
        return f'{costs[money-c] + 1} {i + 1}'
    costs[c] = i