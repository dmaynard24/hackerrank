import re


def validate_postal_code(pc):
  is_integer_in_range = r'\d{6}$'
  has_alternating_repetitive_digit_pair = r'(\d)(?=\d\1)'

  return bool(re.match(
      is_integer_in_range,
      pc)) and len(re.findall(has_alternating_repetitive_digit_pair, pc)) < 2