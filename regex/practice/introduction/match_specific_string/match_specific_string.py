import re


def match_specific_string(test_s, match_s):
  count = len(re.findall(r'%s' % match_s, test_s))
  return f'Number of matches : {count}'