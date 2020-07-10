def wrapper(f):
  def to_phone(s):
    if s.startswith('+91'):
      return f'{s[:3]} {s[3:8]} {s[8:13]}'
    elif s.startswith('91') and len(s) == 12:
      return f'+91 {s[2:7]} {s[7:12]}'
    elif s.startswith('0'):
      return f'+91 {s[1:6]} {s[6:11]}'
    else:
      return f'+91 {s[:5]} {s[5:10]}'

  def fun(l):
    return f(list(map(to_phone, l)))

  return fun


@wrapper
def mobile_numbers(l):
  return '\n'.join(sorted(l))
