import re


def match_x_y_repetitions(test_s):
  return str(bool(re.match(r'^\d{1,2}[a-zA-Z]{3,}\.{,3}$', test_s))).lower()
