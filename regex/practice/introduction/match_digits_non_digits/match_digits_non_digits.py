import re


def match_digits_non_digits(test_s):
  return str(bool(re.match(r'(\d\d\D){2}\d{4}', test_s))).lower()