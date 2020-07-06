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


# html_parser_1('''<html><head><title>HTML Parser - I</title></head>
# <body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>''')