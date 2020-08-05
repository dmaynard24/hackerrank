import re


def match_zero_or_more_repetitions(test_s):
  return str(bool(re.match(r'^\d{2,}[a-z]*[A-Z]*$', test_s))).lower()
