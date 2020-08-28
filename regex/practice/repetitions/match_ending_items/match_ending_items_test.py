import unittest, match_ending_items


class TestMatchEndingItems(unittest.TestCase):
  def test_match_ending_items(self):
    self.assertEqual(match_ending_items.match_ending_items('Kites'), 'true')

  def test_match_ending_items_1(self):
    self.assertEqual(match_ending_items.match_ending_items('Kite'), 'false')


if __name__ == '__main__':
  unittest.main()
