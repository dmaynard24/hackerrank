import numpy


def mean_var_and_std(a):
  print(numpy.mean(a, axis=1))
  print(numpy.var(a, axis=0))
  print(numpy.std(a))