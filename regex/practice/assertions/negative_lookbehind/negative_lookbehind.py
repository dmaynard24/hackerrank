import re


def negative_lookbehind(test_s):
  count = len(re.findall(r'(?<![aeiouAEIOU]).', test_s))
  return f'Number of matches : {count}'
