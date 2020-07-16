import unittest, complex_numbers


class TestArrays(unittest.TestCase):
  def test_complex_numbers(self):
    self.assertEqual(
        complex_numbers.complex_numbers([2, 1], [5, 6]), '''7.00+7.00i
-3.00-5.00i
4.00+17.00i
0.26-0.11i
2.24+0.00i
7.81+0.00i''')


if __name__ == '__main__':
  unittest.main()