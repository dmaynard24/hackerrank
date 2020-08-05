import re


def get_domain_names(code):
  d = [
      re.sub(r'^(www|ww2)\.', '', d)
      for d in re.findall(r'(?<=://)((?:[\w\-]+\.)+[a-zA-Z0-9]+)', code)
  ]
  return ';'.join(sorted(set(d)))