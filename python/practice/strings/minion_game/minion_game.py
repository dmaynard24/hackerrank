def minion_game(string):
  vowels = {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1}
  s = 0
  k = 0
  for i, char in enumerate(string):
    if char in vowels:
      k += len(string) - i
    else:
      s += len(string) - i
  if s > k:
    return f'Stuart {s}'
  elif s < k:
    return f'Kevin {k}'
  else:
    return 'Draw'