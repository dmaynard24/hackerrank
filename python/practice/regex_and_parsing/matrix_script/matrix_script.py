import re, itertools


def matrix_script(matrix):
  s = ''.join(itertools.chain(*list(zip(*matrix))))
  alpha_num = 'a-zA-Z0-9'
  return re.sub(
      r'(?<=[{}])[^{}_]+(?=[{}])'.format(alpha_num, alpha_num, alpha_num), ' ',
      s)
