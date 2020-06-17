from itertools import combinations


def iterables_and_iterators(l, n, k):
  combos = list(combinations(n, k))
  count = 0
  for c in combos:
    if 'a' in c:
      count += 1
  return count / len(combos)