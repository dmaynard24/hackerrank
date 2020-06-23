import string


def ginorts(s):
  order = string.ascii_letters + '1357902468'
  return ''.join(sorted(s, key=order.index))