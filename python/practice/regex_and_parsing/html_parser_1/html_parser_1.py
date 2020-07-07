from html.parser import HTMLParser


def html_parser_1(html):
  class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
      print('Start :', tag)
      for attr in attrs:
        print(f'-> {attr[0]} > {attr[1]}')

    def handle_startendtag(self, tag, attrs):
      print('Empty :', tag)
      for attr in attrs:
        print(f'-> {attr[0]} > {attr[1]}')

    def handle_endtag(self, tag):
      print('End   :', tag)

  parser = MyHTMLParser()
  parser.feed(html)
  parser.close()