def freqQuery(queries):
  output = []

  data_counts = {}
  count_counts = {}
  for query in queries:
    [operation, data] = query
    if operation == 1:
      data_counts[data] = data_counts.get(data, 0) + 1
      count_counts[data_counts[data]] = count_counts.get(data_counts[data],
                                                         0) + 1
    elif operation == 2:
      data_counts[data] = max(0, data_counts.get(data, 1) - 1)
      count_counts[data_counts[data]] = max(
          0,
          count_counts.get(data_counts[data], 1) - 1)
    elif operation == 3:
      if data in count_counts and count_counts[data] > 0:
        output.append(1)
      else:
        output.append(0)

  return output


print(freqQuery([
    [1, 1],
    [2, 2],
    [3, 2],
    [1, 1],
    [1, 1],
    [2, 1],
    [3, 2],
]))  # [0, 1]

print(
    freqQuery([[1, 5], [1, 6], [3, 2], [1, 10], [1, 10], [1, 6], [2, 5],
               [3, 2]]))  # [0, 1]

print(
    freqQuery([[1, 3], [2, 3], [3, 2], [1, 4], [1, 5], [1, 5], [1, 4], [3, 2],
               [2, 4], [3, 2]]))  # [0, 1, 1]
