import re


def is_valid_alien_username(s):
  return bool(re.match(r'^[_\.]\d+[a-zA-Z]*(_?)$', s))