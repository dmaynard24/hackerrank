import numpy


def concatenate(arrs):
  return str(numpy.concatenate([[a] for a in arrs]))