import unittest, mini_max_sum


class TestMiniMaxSum(unittest.TestCase):
  def test_mini_max_sum(self):
    self.assertEqual(mini_max_sum.mini_max_sum([1, 3, 5, 7, 9]), '16 24')
    self.assertEqual(mini_max_sum.mini_max_sum([1, 2, 3, 4, 5]), '10 14')
    self.assertEqual(mini_max_sum.mini_max_sum([7, 69, 2, 221, 8_974]),
                     '299 9271')


if __name__ == '__main__':
  unittest.main()
