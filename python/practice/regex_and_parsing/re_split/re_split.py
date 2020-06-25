import re


def re_split(s):
  return '\n'.join(re.split(r'[,.]', s))