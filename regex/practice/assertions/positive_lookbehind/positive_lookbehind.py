import re


def positive_lookbehind(test_s):
  count = len(re.findall(r'(?<=[13579])\d', test_s))
  return f'Number of matches : {count}'
