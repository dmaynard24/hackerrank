import unittest, minimum_swaps


class TestMinimumSwaps(unittest.TestCase):
  def test_minimum_swaps(self):
    self.assertEqual(minimum_swaps.minimum_swaps([2, 3, 4, 1, 5]), 3)
    self.assertEqual(minimum_swaps.minimum_swaps([1, 3, 5, 2, 4, 6, 7]), 3)


if __name__ == '__main__':
  unittest.main()
