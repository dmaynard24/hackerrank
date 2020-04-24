import unittest, diagonal_difference


class TestDiagonalDifference(unittest.TestCase):
  def test_diagonal_difference(self):
    self.assertEqual(
        diagonal_difference.diagonal_difference([[1, 2, 3], [4, 5, 6],
                                                 [9, 8, 9]]), 2)
    self.assertEqual(
        diagonal_difference.diagonal_difference([[11, 2, 4], [4, 5, 6],
                                                 [10, 8, -12]]), 15)


if __name__ == '__main__':
  unittest.main()
