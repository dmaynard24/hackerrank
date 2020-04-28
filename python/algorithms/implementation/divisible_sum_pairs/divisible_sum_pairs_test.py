import unittest, divisible_sum_pairs


class TestDivisibleSumPairs(unittest.TestCase):
  def test_divisible_sum_pairs(self):
    self.assertEqual(
        divisible_sum_pairs.divisible_sum_pairs(6, 5, [1, 2, 3, 4, 5, 6]), 3)
    self.assertEqual(
        divisible_sum_pairs.divisible_sum_pairs(6, 3, [1, 3, 2, 6, 1, 2]), 5)


if __name__ == '__main__':
  unittest.main()
