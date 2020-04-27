import unittest, count_apples_and_oranges


class TestCountApplesAndOranges(unittest.TestCase):
  def test_count_apples_and_oranges(self):
    self.assertEqual(
        count_apples_and_oranges.count_apples_and_oranges(
            7, 10, 4, 12, [2, 3, -4], [3, -2, -4]), [1, 2])
    self.assertEqual(
        count_apples_and_oranges.count_apples_and_oranges(
            7, 11, 5, 15, [-2, 2, 1], [5, -6]), [1, 1])


if __name__ == '__main__':
  unittest.main()
