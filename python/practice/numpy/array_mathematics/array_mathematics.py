import numpy


def array_mathematics(a, b):
  a, b = [a], [b]
  print(numpy.add(a, b))
  print(numpy.subtract(a, b))
  print(numpy.multiply(a, b))
  print(numpy.floor_divide(a, b))
  print(numpy.mod(a, b))
  print(numpy.power(a, b))