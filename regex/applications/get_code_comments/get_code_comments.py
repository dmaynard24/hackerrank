import re


def get_code_comments(code):
  # first strip whitespace from left side of each new line
  code = re.sub(r'\n\s*', '\n', code)
  comments = re.findall(r'\/\/.*|\/\*[\s\S]*?\*\/', code)
  return '\n'.join(comments)