import re


def detect_html_links(html):
  l = re.findall(r'href="(.+?)".*?>(.*?)(?=</a>)', html)
  l = [(t[0], re.sub(r'<(\/)?.+?>', '', t[1]).strip()) for t in l]
  return '\n'.join([','.join(t) for t in l])
