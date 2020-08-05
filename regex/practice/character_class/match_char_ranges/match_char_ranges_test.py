import unittest, match_char_ranges


class TestMatchCharRanges(unittest.TestCase):
  def test_match_char_ranges(self):
    self.assertEqual(match_char_ranges.match_char_ranges('h4CkR'), 'true')


if __name__ == '__main__':
  unittest.main()
