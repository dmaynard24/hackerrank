import unittest, arithmetic_operators


class TestArithmeticOperators(unittest.TestCase):
  def test_arithmetic_operators(self):
    self.assertEqual(arithmetic_operators.add(3, 2), 5)
    self.assertEqual(arithmetic_operators.subtract(3, 2), 1)
    self.assertEqual(arithmetic_operators.multiply(3, 2), 6)


if __name__ == '__main__':
  unittest.main()
