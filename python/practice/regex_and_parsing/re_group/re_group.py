import re


def re_group(s):
  m = re.search(r'([a-zA-Z0-9])\1', s)
  return m.group(1) if m else '-1'