import unittest, set_difference


class TestSetDifference(unittest.TestCase):
  def test_set_difference(self):
    self.assertEqual(
        set_difference.set_difference([1, 2, 3, 4, 5, 6, 7, 8, 9],
                                      [10, 1, 2, 3, 11, 21, 55, 6, 8]), 4)


if __name__ == '__main__':
  unittest.main()
