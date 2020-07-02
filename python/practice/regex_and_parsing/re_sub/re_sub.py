import re


def re_sub(s):
  return re.sub(r'(?<= )(&&|\|\|)(?= )', lambda m: 'and'
                if m.group() == '&&' else 'or', s)
