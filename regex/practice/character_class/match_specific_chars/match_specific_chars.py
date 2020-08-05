import re


def match_specific_chars(test_s):
  return str(bool(re.match(r'^[1-3][0-2][xs0][30Aa][xsu][\.,]$',
                           test_s))).lower()
