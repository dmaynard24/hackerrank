import re


def exclude_specific_chars(test_s):
  return str(
      bool(re.match(r'^[^\d][^aeiou][^bcDF][^\s][^AEIOU][^\.,]$',
                    test_s))).lower()
