import numpy


def min_and_max(a):
  mini = numpy.min(a, axis=1)
  return numpy.max(mini)