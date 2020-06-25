import re


def detect_float(s):
  return bool(re.match(r'[+-]?\d*\.\d+$', s))
