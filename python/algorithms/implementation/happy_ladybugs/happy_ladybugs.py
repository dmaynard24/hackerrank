def happy_ladybugs(b):
  if len(b) == 1:
    return 'YES' if b[0] == '_' else 'NO'

  is_in_order = True
  char_counts = {}
  # set first and last char_count
  char_counts[b[0]] = char_counts.get(b[0], 0) + 1
  char_counts[b[-1]] = char_counts.get(b[-1], 0) + 1
  # set remaining char_counts while also checking for order
  for i in range(1, len(b) - 1):
    is_in_order = is_in_order and (b[i - 1] == b[i] or b[i + 1] == b[i])
    char_counts[b[i]] = char_counts.get(b[i], 0) + 1

  is_happy = True
  for char in char_counts:
    if char != '_' and char_counts[char] < 2:
      is_happy = False
      break

  if '_' not in char_counts:
    return 'YES' if is_happy and is_in_order else 'NO'
  return 'YES' if is_happy else 'NO'