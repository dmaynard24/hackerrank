def zipped(scores, n):
  z = zip(*scores)
  return [sum(marks) / n for marks in z]