import unittest, reduce
from fractions import Fraction


class TestReduce(unittest.TestCase):
  def test_reduce(self):
    self.assertEqual(
        reduce.practice_reduce(
            [Fraction(1, 2), Fraction(3, 4),
             Fraction(10, 6)]), (5, 8))


if __name__ == '__main__':
  unittest.main()