def athlete_sort(arr, k):
  return '\n'.join(
      [' '.join(map(str, a)) for a in sorted(arr, key=lambda attr: attr[k])])
