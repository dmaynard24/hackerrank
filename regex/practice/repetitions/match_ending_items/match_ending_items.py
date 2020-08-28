import re


def match_ending_items(test_s):
  return str(bool(re.match(r'^[a-zA-Z]*s$', test_s))).lower()
