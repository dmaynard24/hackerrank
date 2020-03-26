import unittest, hourglass_sum


class TestHourglassSum(unittest.TestCase):
  def test_hourglass_sum(self):
    self.assertEqual(
        hourglass_sum.hourglass_sum([[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0],
                                     [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0],
                                     [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]),
        19)
    self.assertEqual(
        hourglass_sum.hourglass_sum([[-9, -9, -9, 1, 1,
                                      1], [0, -9, 0, 4, 3, 2],
                                     [-9, -9, -9, 1, 2, 3], [0, 0, 8, 6, 6, 0],
                                     [0, 0, 0, -2, 0, 0], [0, 0, 1, 2, 4, 0]]),
        28)


if __name__ == '__main__':
  unittest.main()
