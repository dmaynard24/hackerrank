import re


def capturing_and_non_capturing_groups(test_s):
  return str(bool(re.search(r'(ok){3,}', test_s))).lower()