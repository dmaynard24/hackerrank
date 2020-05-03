def angry_professor(k, a):
  early_count = 0
  for time in a:
    if time <= 0:
      early_count += 1
  return 'NO' if early_count >= k else 'YES'