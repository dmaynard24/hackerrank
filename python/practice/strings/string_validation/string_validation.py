import re


def string_validation(s):
  bools = []
  bools.append(bool(re.search('[a-zA-Z0-9]', s)))
  bools.append(bool(re.search('[a-zA-Z]', s)))
  bools.append(bool(re.search('[0-9]', s)))
  bools.append(bool(re.search('[a-z]', s)))
  bools.append(bool(re.search('[A-Z]', s)))
  return bools