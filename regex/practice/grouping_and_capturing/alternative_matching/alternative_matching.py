import re


def alternative_matching(test_s):
  return str(bool(re.match(r'^(Mr\.|Mrs\.|Ms\.|Dr\.|Er.)[a-zA-Z]+$',
                           test_s))).lower()
