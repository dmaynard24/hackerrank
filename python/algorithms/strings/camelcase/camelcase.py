def camelcase(s):
  return len([c for c in s if str.isupper(c)]) + 1