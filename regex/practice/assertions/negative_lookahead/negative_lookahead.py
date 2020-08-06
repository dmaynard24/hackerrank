import re


def negative_lookahead(test_s):
  count = len(re.findall(r'(.)(?!\1)', test_s))
  return f'Number of matches : {count}'
