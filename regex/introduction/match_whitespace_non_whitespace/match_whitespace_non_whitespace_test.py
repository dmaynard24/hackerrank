import unittest, match_whitespace_non_whitespace


class TestMatchWhitespaceNonWhitespace(unittest.TestCase):
  def test_match_whitespace_non_whitespace(self):
    self.assertEqual(
        match_whitespace_non_whitespace.match_whitespace_non_whitespace(
            '12 11 15'), 'true')


if __name__ == '__main__':
  unittest.main()
