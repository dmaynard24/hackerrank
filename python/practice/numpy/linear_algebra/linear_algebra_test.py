import unittest, linear_algebra


class TestLinearAlgebra(unittest.TestCase):
  def test_linear_algebra(self):
    self.assertEqual(linear_algebra.linear_algebra([[1.1, 1.1], [1.1, 1.1]]),
                     0.0)


if __name__ == '__main__':
  unittest.main()