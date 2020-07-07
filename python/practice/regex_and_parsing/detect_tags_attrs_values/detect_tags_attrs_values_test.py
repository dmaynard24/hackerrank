from io import StringIO
from unittest.mock import patch
import unittest, detect_tags_attrs_values


class TestDetectTagsAttrsValues(unittest.TestCase):
  def test_detect_tags_attrs_values(self):
    with patch('sys.stdout', new=StringIO()) as fake_out:
      detect_tags_attrs_values.detect_tags_attrs_values('''<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">
  <!-- <param name="movie" value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>''')
      self.assertEqual(
          fake_out.getvalue(), '''head
title
object
-> type > application/x-flash
-> data > your-file.swf
-> width > 0
-> height > 0
param
-> name > quality
-> value > high
''')


if __name__ == '__main__':
  unittest.main()
