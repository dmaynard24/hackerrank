import unittest, super_digit


class TestSuperDigit(unittest.TestCase):
  def test_super_digit(self):
    self.assertEqual(super_digit.super_digit('148', 3), 3)
    self.assertEqual(super_digit.super_digit('9875', 4), 8)
    self.assertEqual(super_digit.super_digit('123', 3), 9)


if __name__ == '__main__':
  unittest.main()
