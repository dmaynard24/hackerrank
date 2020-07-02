import re


def validate_phone_number(s):
  return 'YES' if bool(re.fullmatch(r'[789]\d{9}', s)) else 'NO'
