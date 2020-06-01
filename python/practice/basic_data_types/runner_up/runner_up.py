def runner_up(arr):
  arr.sort(reverse=True)
  for i in range(1, len(arr)):
    if arr[i] != arr[i - 1]:
      return arr[i]