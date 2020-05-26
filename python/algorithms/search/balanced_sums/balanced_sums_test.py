import unittest, balanced_sums


class TestBalancedSums(unittest.TestCase):
  def test_balanced_sums(self):
    self.assertEqual(balanced_sums.balanced_sums([1, 2, 3]), 'NO')
    self.assertEqual(balanced_sums.balanced_sums([1, 2, 3, 3]), 'YES')
    self.assertEqual(balanced_sums.balanced_sums([1]), 'YES')
    self.assertEqual(balanced_sums.balanced_sums([2, 0, 0, 0]), 'YES')


if __name__ == '__main__':
  unittest.main()
