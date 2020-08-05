import re


def match_word_non_word(test_s):
  return str(bool(re.match(r'\w{3}\W\w{10}\W\w{3}', test_s))).lower()