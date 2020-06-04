import textwrap


def text_wrap(string, max_width):
  return '\n'.join(textwrap.wrap(string, max_width))