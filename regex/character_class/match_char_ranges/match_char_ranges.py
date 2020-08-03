import re


def match_char_ranges(test_s):
  return str(bool(re.search(r'^[a-z][1-9][^a-z][^A-Z][A-Z]', test_s))).lower()
