import itertools


def permutations(s, k):
  return '\n'.join(
      map(lambda p: ''.join(p), itertools.permutations(sorted(s), int(k))))
