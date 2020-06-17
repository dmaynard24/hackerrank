import itertools


def combinations_with_replacement(s, k):
  return '\n'.join([
      ''.join(c)
      for c in itertools.combinations_with_replacement(sorted(s), int(k))
  ])
