import unittest, missing_numbers


class TestMissingNumbers(unittest.TestCase):
  def test_missing_numbers(self):
    self.assertEqual(
        missing_numbers.missing_numbers(
            [203, 204, 205, 206, 207, 208, 203, 204, 205, 206],
            [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]),
        [204, 205, 206])
    self.assertEqual(
        missing_numbers.missing_numbers(
            [11, 4, 11, 7, 13, 4, 12, 11, 10, 14],
            [11, 4, 11, 7, 3, 7, 10, 13, 4, 8, 12, 11, 10, 14, 12]),
        [3, 7, 8, 10, 12])


if __name__ == '__main__':
  unittest.main()
