import re


def validate_credit_card(cc):
  is_valid_without_hyphens = len(cc) == 16 and bool(re.match(
      r'[4-6]', cc)) and not re.search(r'[^\d]', cc) and not re.search(
          r'(\d)\1\1\1', cc)

  is_valid_with_hyphens = len(cc) == 19 and bool(re.match(
      r'[4-6]', cc)) and bool(
          re.match(r'(\d{4}-){3}\d{4}',
                   cc)) and not re.search(r'(\d)\1\1\1', cc.replace('-', ''))

  return is_valid_without_hyphens or is_valid_with_hyphens