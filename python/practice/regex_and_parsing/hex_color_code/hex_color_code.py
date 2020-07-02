import re


def hex_color_code(s):
  props = re.findall(r'(?<=:).[^}]*(?=;)', s)

  matches = []
  for p in props:
    matches.extend([
        ''.join(m)
        for m in re.findall(r'(#[a-fA-F0-9]{6})|(#[a-fA-F0-9]{3})', p)
    ])

  return '\n'.join(matches)