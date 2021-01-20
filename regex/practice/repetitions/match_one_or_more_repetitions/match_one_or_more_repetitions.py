import re


def match_one_or_more_repetitions(test_s):
  return str(bool(re.match(r'^\d+[A-Z]+[a-z]+$', test_s))).lower()
