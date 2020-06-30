import re


def re_findall(s):
  c = 'qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM'
  v = 'aeiouAEIOU'
  matches = re.findall(r'(?<=[%s])([%s]{2,})(?=[%s])' % (c, v, c), s)
  return '\n'.join(matches) if matches else -1