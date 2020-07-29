import re


def detect_html_attrs(html):
  opening_tags = re.findall(r'(<\w+(?: [\s\S]+?)?>)', html)

  tags = []
  for ot in opening_tags:
    ot = re.sub(r'=\'([\s\S]*)\'', r'="\1"', ot)
    tag = re.search(r'(?<=<)(\w+)', ot).group(0)
    attrs = re.findall(r'(?<= )([a-zA-Z\-_]+)(?==")', ot)
    tags.append([tag] + attrs)

  tags_dict = {}
  for t in tags:
    tags_dict[t[0]] = tags_dict.get(t[0], set())
    for i in range(1, len(t)):
      tags_dict[t[0]].add(t[i])

  tag_attrs = [f'{k}:{",".join(sorted(tags_dict[k]))}' for k in tags_dict]
  return '\n'.join(sorted(tag_attrs))