def pangram(s):
  return 'pangram' if len(set(str.lower(s).replace(
      ' ', ''))) == 26 else 'not pangram'
