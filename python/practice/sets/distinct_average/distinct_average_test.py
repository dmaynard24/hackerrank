import unittest, distinct_average


class TestDistinctAverage(unittest.TestCase):
  def test_distinct_average(self):
    self.assertEqual(
        distinct_average.distinct_average(
            [161, 182, 161, 154, 176, 170, 167, 171, 170, 174]), 169.375)


if __name__ == '__main__':
  unittest.main()
