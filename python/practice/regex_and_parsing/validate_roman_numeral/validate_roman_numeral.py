import re


def validate_roman_numeral(rn):
  return bool(
      re.match(r'M{0,3}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$', rn))
