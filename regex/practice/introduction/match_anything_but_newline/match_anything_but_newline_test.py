import unittest, match_anything_but_newline


class TestMatchAnythingButNewline(unittest.TestCase):
  def test_match_anything_but_newline(self):
    self.assertEqual(
        match_anything_but_newline.match_anything_but_newline(
            '123.456.abc.def'), 'true')

  def test_match_anything_but_newline_1(self):
    self.assertEqual(
        match_anything_but_newline.match_anything_but_newline(
            '1123.456.abc.def'), 'false')


if __name__ == '__main__':
  unittest.main()
