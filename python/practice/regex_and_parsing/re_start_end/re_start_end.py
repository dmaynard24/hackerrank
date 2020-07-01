import re


def re_start_end(s, k):
  if k not in s:
    return '(-1, -1)'
  else:
    matches = re.finditer(r'(?={})'.format(k), s)
    return '\n'.join(
        [str((m.start(), m.start() + len(k) - 1)) for m in matches])
