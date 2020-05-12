def circular_array_rotation(a, k, queries):
  return [a[(query - k) % len(a)] for query in queries]