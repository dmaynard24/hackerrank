import unittest, symmetric_difference_operation


class TestSetIntersection(unittest.TestCase):
  def test_symmetric_difference_operation(self):
    self.assertEqual(
        symmetric_difference_operation.symmetric_difference_operation(
            [1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 1, 2, 3, 11, 21, 55, 6, 8]), 8)


if __name__ == '__main__':
  unittest.main()
