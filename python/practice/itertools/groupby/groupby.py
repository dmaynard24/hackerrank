import itertools


def groupby(s):
  return ' '.join(
      map(str, [(len(list(g)), int(k)) for k, g in itertools.groupby(s)]))
