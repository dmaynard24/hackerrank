import unittest, array_manipulation


class TestArrayManipulation(unittest.TestCase):
  def test_array_manipulation(self):
    self.assertEqual(
        array_manipulation.array_manipulation(
            5, [[1, 2, 100], [2, 5, 100], [3, 4, 100]]), 200)
    self.assertEqual(
        array_manipulation.array_manipulation(
            10, [[1, 5, 3], [4, 8, 7], [6, 9, 1]]), 10)
    self.assertEqual(
        array_manipulation.array_manipulation(
            4, [[2, 3, 603], [1, 1, 286], [4, 4, 882]]), 882)


if __name__ == '__main__':
  unittest.main()
