def array_manipulation(n, queries):
  arr = [0] * n
  for query in queries:
    [a, b, k] = query
    for i in range(a - 1, b):
      arr[i] += k
  return max(arr)


print(array_manipulation(5, [[1, 2, 100], [2, 5, 100], [3, 4, 100]]))  # 200
