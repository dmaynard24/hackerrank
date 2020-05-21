def funny_string(s):
  ords = [ord(char) for char in s]
  for i in range(len(ords) - 1):
    if abs(ords[i] - ords[i + 1]) != abs(ords[len(ords) -
                                              (i + 1)] - ords[len(ords) -
                                                              (i + 2)]):
      return 'Not Funny'
  return 'Funny'