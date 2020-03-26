import sys


def hourglass_sum(arr):
  largest_sum = -sys.maxsize
  max_y = len(arr) - 1
  max_x = len(arr[0]) - 1
  for y in range(1, max_y):
    for x in range(1, max_x):
      this_sum = arr[y - 1][x - 1] + arr[y - 1][x] + arr[y - 1][x + 1] + arr[
          y][x] + arr[y + 1][x - 1] + arr[y + 1][x] + arr[y + 1][x + 1]
      largest_sum = max(largest_sum, this_sum)
  return largest_sum