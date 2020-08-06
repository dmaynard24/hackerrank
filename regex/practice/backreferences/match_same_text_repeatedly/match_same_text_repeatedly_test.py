import unittest, match_same_text_repeatedly


class TestMatchSameTextRepeatedly(unittest.TestCase):
  def test_match_same_text_repeatedly(self):
    self.assertEqual(
        match_same_text_repeatedly.match_same_text_repeatedly(
            'ab #1?AZa$ab #1?AZa$'), 'true')


if __name__ == '__main__':
  unittest.main()
