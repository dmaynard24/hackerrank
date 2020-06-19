import re


def incorrect_regex(s):
  try:
    re.compile(s)
    return True
  except BaseException:
    return False