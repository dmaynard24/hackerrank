import re


def match_word_boundaries(test_s):
  return str(bool(re.search(r'\b[aeiouAEIOU][a-zA-Z]*\b', test_s))).lower()