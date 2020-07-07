from html.parser import HTMLParser


def detect_tags_attrs_values(html):
  class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
      print(tag)
      for attr in attrs:
        print(f'-> {attr[0]} > {attr[1]}')

    def handle_startendtag(self, tag, attrs):
      print(tag)
      for attr in attrs:
        print(f'-> {attr[0]} > {attr[1]}')

  parser = MyHTMLParser()
  parser.feed(html)
  parser.close()