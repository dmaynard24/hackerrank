import unittest, is_subset


class TestIsSubset(unittest.TestCase):
  def test_is_subset(self):
    self.assertEqual(
        is_subset.is_subset([1, 2, 3, 5, 6], [9, 8, 5, 6, 3, 2, 1, 4, 7]),
        True)

  def test_is_subset_1(self):
    self.assertEqual(is_subset.is_subset([2], [3, 6, 5, 4, 1]), False)

  def test_is_subset_2(self):
    self.assertEqual(is_subset.is_subset([1, 2, 3, 5, 6, 8, 9], [9, 8, 2]),
                     False)


if __name__ == '__main__':
  unittest.main()
