def surface_area(A):
  sa = 0

  for row in range(len(A)):
    for col in range(len(A[row])):
      if A[row][col] == 0:
        continue

      curr = A[row][col]

      # always add top and bottom face of cube
      sa += 2

      # above
      if row - 1 < 0:
        sa += curr
      elif A[row - 1][col] < curr:
        sa += curr - A[row - 1][col]

      # to the right
      if col + 1 > len(A[row]) - 1:
        sa += curr
      elif A[row][col + 1] < curr:
        sa += curr - A[row][col + 1]

      # below
      if row + 1 > len(A) - 1:
        sa += curr
      elif A[row + 1][col] < curr:
        sa += curr - A[row + 1][col]

      # to the left
      if col - 1 < 0:
        sa += curr
      elif A[row][col - 1] < curr:
        sa += curr - A[row][col - 1]

  return sa