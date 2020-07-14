import unittest, polynomials


class TestPolynomials(unittest.TestCase):
  def test_polynomials(self):
    self.assertEqual(polynomials.polynomials([1.1, 2, 3], 0), 3.0)


if __name__ == '__main__':
  unittest.main()