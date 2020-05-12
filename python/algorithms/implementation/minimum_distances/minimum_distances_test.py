import unittest, minimum_distances


class TestMinimumDistances(unittest.TestCase):
  def test_minimum_distances(self):
    self.assertEqual(minimum_distances.minimum_distances([7, 1, 3, 4, 1, 7]),
                     3)
    self.assertEqual(minimum_distances.minimum_distances([1, 2, 3, 4, 10]), -1)


if __name__ == '__main__':
  unittest.main()
