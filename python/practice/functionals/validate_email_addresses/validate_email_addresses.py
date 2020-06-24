import re


def is_valid_email(s):
  return re.match(r'[\w|\-]+@[a-zA-Z\d]+\.\S{1,3}$', s)


def validate_email_addresses(emails):
  return sorted(list(filter(is_valid_email, emails)))
