import re


def positive_lookahead(test_s):
  count = len(re.findall(r'o(?=oo)', test_s))
  return f'Number of matches : {count}'
