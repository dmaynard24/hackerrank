import unittest, square_loop


class TestSquareLoop(unittest.TestCase):
  def test_square_loop(self):
    self.assertEqual(square_loop.square_loop(5), [0, 1, 4, 9, 16])


if __name__ == '__main__':
  unittest.main()
