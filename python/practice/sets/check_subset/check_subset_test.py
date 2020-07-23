import unittest, check_subset


class TestCheckSubset(unittest.TestCase):
  def test_check_subset(self):
    self.assertEqual(
        check_subset.check_subset([1, 2, 3, 5, 6],
                                  [9, 8, 5, 6, 3, 2, 1, 4, 7]), True)

  def test_check_subset_1(self):
    self.assertEqual(check_subset.check_subset([2], [3, 6, 5, 4, 1]), False)

  def test_check_subset_2(self):
    self.assertEqual(
        check_subset.check_subset([1, 2, 3, 5, 6, 8, 9], [9, 8, 2]), False)


if __name__ == '__main__':
  unittest.main()
