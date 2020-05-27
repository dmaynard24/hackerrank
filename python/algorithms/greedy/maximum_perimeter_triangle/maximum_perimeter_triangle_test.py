import unittest, maximum_perimeter_triangle


class TestMaximumPerimeterTriangle(unittest.TestCase):
  def test_maximum_perimeter_triangle(self):
    self.assertEqual(
        maximum_perimeter_triangle.maximum_perimeter_triangle([1, 1, 1, 3, 3]),
        [1, 3, 3])
    self.assertEqual(
        maximum_perimeter_triangle.maximum_perimeter_triangle([1, 2, 3]), [-1])
    self.assertEqual(
        maximum_perimeter_triangle.maximum_perimeter_triangle(
            [1, 1, 1, 2, 3, 5]), [1, 1, 1])


if __name__ == '__main__':
  unittest.main()
