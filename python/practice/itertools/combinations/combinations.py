import itertools


def combinations(s, k):
  combos = []
  for i in range(1, int(k) + 1):
    combos.extend(
        [''.join(c) for c in list(itertools.combinations(sorted(s), i))])
  return '\n'.join(combos)