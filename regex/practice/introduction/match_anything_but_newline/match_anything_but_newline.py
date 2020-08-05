import re


def match_anything_but_newline(test_s):
  return str(bool(re.match(r'(...\.){3}...$', test_s))).lower()