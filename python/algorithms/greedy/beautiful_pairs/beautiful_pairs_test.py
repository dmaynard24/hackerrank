import unittest, beautiful_pairs


class TestBeautifulPairs(unittest.TestCase):
  def test_beautiful_pairs(self):
    self.assertEqual(
        beautiful_pairs.beautiful_pairs([1, 2, 3, 4], [1, 2, 3, 3]), 4)
    self.assertEqual(
        beautiful_pairs.beautiful_pairs([3, 5, 7, 11, 5, 8],
                                        [5, 7, 11, 10, 5, 8]), 6)


if __name__ == '__main__':
  unittest.main()
