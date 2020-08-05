import re


def get_programming_lang(code):
  if bool(re.search(r'import java', code)):
    return 'Java'
  elif bool(re.search(r'{', code)):
    return 'C'
  else:
    return 'Python'