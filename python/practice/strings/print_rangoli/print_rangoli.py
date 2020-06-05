def print_rangoli(size):
  w = size * 4 - 3
  rows = [
      '-'.join([chr(j + 96) for j in range(size, i, -1)] +
               [chr(j + 96) for j in range(i + 2, size + 1)]).center(w, '-')
      for i in range(size)
  ]
  return '\n'.join(rows[:0:-1] + rows)