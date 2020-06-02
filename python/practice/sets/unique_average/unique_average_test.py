import unittest, unique_average


class TestUniqueAverage(unittest.TestCase):
  def test_unique_average(self):
    self.assertEqual(
        unique_average.unique_average(
            [161, 182, 161, 154, 176, 170, 167, 171, 170, 174]), 169.375)


if __name__ == '__main__':
  unittest.main()
