import unittest, match_specific_chars


class TestMatchSpecificChars(unittest.TestCase):
  def test_match_specific_chars(self):
    self.assertEqual(match_specific_chars.match_specific_chars('1203x.'),
                     'true')


if __name__ == '__main__':
  unittest.main()
