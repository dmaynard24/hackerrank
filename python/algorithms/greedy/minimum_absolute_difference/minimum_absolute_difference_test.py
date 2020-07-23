import unittest, minimum_absolute_difference


class TestMinimumAbsoluteDifference(unittest.TestCase):
  def test_minimum_absolute_difference(self):
    self.assertEqual(
        minimum_absolute_difference.minimum_absolute_difference([3, -7, 0]), 3)

  def test_minimum_absolute_difference_1(self):
    self.assertEqual(
        minimum_absolute_difference.minimum_absolute_difference(
            [-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]), 1)

  def test_minimum_absolute_difference_2(self):
    self.assertEqual(
        minimum_absolute_difference.minimum_absolute_difference(
            [1, -3, 71, 68, 17]), 3)


if __name__ == '__main__':
  unittest.main()
