from html.parser import HTMLParser


def html_parser_2(html):
  class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
      if data != '\n':
        print('>>> Data')
        print(data)

    def handle_comment(self, data):
      if data.find('\n') > -1:
        print('>>> Multi-line Comment')
      else:
        print('>>> Single-line Comment')
      print(data)

  parser = MyHTMLParser()
  parser.feed(html)
  parser.close()