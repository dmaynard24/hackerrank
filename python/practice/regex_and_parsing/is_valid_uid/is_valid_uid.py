import re


def is_valid_uid(uid):
  u = ''.join(sorted(uid))
  return len(u) == 10 and not re.search(r'[^a-zA-Z0-9]', u) and re.search(
      r'[A-Z]{2}', u) and re.search(r'[0-9]{3}',
                                    u) and not re.search(r'(.)\1', u)
