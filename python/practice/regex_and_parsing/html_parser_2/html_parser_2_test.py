from io import StringIO
from unittest.mock import patch
import unittest, html_parser_2


class TestHtmlParser2(unittest.TestCase):
  def test_html_parser_2(self):
    with patch('sys.stdout', new=StringIO()) as fake_out:
      html_parser_2.html_parser_2('''<!--[if IE 9]>IE9-specific content
<![endif]-->
<div> Welcome to HackerRank</div>
<!--[if IE 9]>IE9-specific content<![endif]-->''')
      self.assertEqual(
          fake_out.getvalue(), '''>>> Multi-line Comment
[if IE 9]>IE9-specific content
<![endif]
>>> Data
 Welcome to HackerRank
>>> Single-line Comment
[if IE 9]>IE9-specific content<![endif]
''')


if __name__ == '__main__':
  unittest.main()
