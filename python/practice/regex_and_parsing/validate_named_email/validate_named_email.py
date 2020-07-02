import re


def validate_named_email(s):
  e = s.split()[1]
  return bool(re.match(r'<[a-zA-Z0-9]+[\w\-\.]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>', e))