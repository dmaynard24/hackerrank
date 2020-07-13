import numpy


def sum_and_prod(arr):
  s = numpy.sum(arr, axis=0)
  return numpy.prod(s)