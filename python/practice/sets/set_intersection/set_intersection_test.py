import unittest, set_intersection


class TestSetIntersection(unittest.TestCase):
  def test_set_intersection(self):
    self.assertEqual(
        set_intersection.set_intersection([1, 2, 3, 4, 5, 6, 7, 8, 9],
                                          [10, 1, 2, 3, 11, 21, 55, 6, 8]), 5)


if __name__ == '__main__':
  unittest.main()
