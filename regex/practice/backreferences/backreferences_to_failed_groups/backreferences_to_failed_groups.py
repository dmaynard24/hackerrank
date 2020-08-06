import re


def backreferences_to_failed_groups(test_s):
  return str(bool(re.match(r'^\d\d(-?)\d\d\1\d\d\1\d\d$', test_s))).lower()
