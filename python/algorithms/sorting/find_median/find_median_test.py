import unittest, find_median


class TestFindMedian(unittest.TestCase):
  def test_find_median(self):
    self.assertEqual(find_median.find_median([0, 1, 2, 4, 6, 5, 3]), 3)


if __name__ == '__main__':
  unittest.main()
