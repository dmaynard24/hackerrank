import re


def match_whitespace_non_whitespace(test_s):
  return str(bool(re.match(r'(\S\S\s){2}\S\S', test_s))).lower()