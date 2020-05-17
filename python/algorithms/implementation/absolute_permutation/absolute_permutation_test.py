import unittest, absolute_permutation


class TestAbsolutePermutation(unittest.TestCase):
  def test_absolute_permutation(self):
    self.assertEqual(absolute_permutation.absolute_permutation(10, 5),
                     [6, 7, 8, 9, 10, 1, 2, 3, 4, 5])
    self.assertEqual(absolute_permutation.absolute_permutation(10, 6), [-1])
    self.assertEqual(absolute_permutation.absolute_permutation(4, 2),
                     [3, 4, 1, 2])
    self.assertEqual(absolute_permutation.absolute_permutation(10, 1),
                     [2, 1, 4, 3, 6, 5, 8, 7, 10, 9])
    self.assertEqual(absolute_permutation.absolute_permutation(10, 0),
                     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    self.assertEqual(absolute_permutation.absolute_permutation(10, 3), [-1])
    self.assertEqual(absolute_permutation.absolute_permutation(9, 1), [-1])
    self.assertEqual(absolute_permutation.absolute_permutation(8, 2),
                     [3, 4, 1, 2, 7, 8, 5, 6])
    self.assertEqual(absolute_permutation.absolute_permutation(12, 2),
                     [3, 4, 1, 2, 7, 8, 5, 6, 11, 12, 9, 10])
    self.assertEqual(absolute_permutation.absolute_permutation(12, 4), [-1])
    self.assertEqual(absolute_permutation.absolute_permutation(16, 4),
                     [5, 6, 7, 8, 1, 2, 3, 4, 13, 14, 15, 16, 9, 10, 11, 12])
    self.assertEqual(absolute_permutation.absolute_permutation(92, 14), [-1])


if __name__ == '__main__':
  unittest.main()
