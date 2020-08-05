import re


def detect_html_tags(html):
  tags = re.findall(r'(?<=</)\w+(?=>)|(?<=<)\w+(?= )', html)
  return ';'.join(sorted(set(tags)))
