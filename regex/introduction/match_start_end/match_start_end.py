import re


def match_start_end(test_s):
  return str(bool(re.match(r'^\d\w{4}.$', test_s))).lower()