import unittest, plus_minus


class TestPlusMinus(unittest.TestCase):
  def test_plus_minus(self):
    self.assertEqual(plus_minus.plus_minus([1, 1, 0, -1, -1]), [0.4, 0.4, 0.2])
    self.assertEqual(plus_minus.plus_minus([-4, 3, -9, 0, 4, 1]),
                     [0.5, 0.3333333333333333, 0.16666666666666666])


if __name__ == '__main__':
  unittest.main()
