def zipped(scores, n):
  z = zip(*scores)
  return '\n'.join([str(sum(marks) / n) for marks in z])