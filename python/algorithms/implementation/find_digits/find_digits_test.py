import unittest, find_digits


class TestFindDigits(unittest.TestCase):
  def test_find_digits(self):
    self.assertEqual(find_digits.find_digits(12), 2)
    self.assertEqual(find_digits.find_digits(1012), 3)


if __name__ == '__main__':
  unittest.main()
