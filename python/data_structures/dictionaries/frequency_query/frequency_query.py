def frequency_query(queries):
  output = []

  data_counts = {}
  count_counts = {}
  for query in queries:
    [operation, data] = query
    if operation == 1:
      if data in data_counts:
        count_counts[data_counts[data]] = count_counts.get(
            data_counts[data], 1) - 1
        data_counts[data] += 1
      else:
        data_counts[data] = 1
      count_counts[data_counts[data]] = count_counts.get(data_counts[data],
                                                         0) + 1
    elif operation == 2:
      if data in data_counts and data_counts[data] > 0:
        count_counts[data_counts[data]] = count_counts.get(
            data_counts[data], 1) - 1
        data_counts[data] -= 1
        count_counts[data_counts[data]] = count_counts.get(
            data_counts[data], 0) + 1
    elif operation == 3:
      if data in count_counts and count_counts[data] > 0:
        output.append(1)
      else:
        output.append(0)

  return output
