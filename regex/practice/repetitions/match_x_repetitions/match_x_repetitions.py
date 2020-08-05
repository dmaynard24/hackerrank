import re


def match_x_repetitions(test_s):
  return str(bool(re.match(r'^[a-zA-Z02468]{40}[\s13579]{5}$',
                           test_s))).lower()
