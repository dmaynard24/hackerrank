import unittest, division


class TestDivision(unittest.TestCase):
  def test_division(self):
    self.assertEqual(division.integer_divide(4, 3), 1)
    self.assertEqual(division.float_divide(4, 3), 1.3333333333333333)


if __name__ == '__main__':
  unittest.main()
