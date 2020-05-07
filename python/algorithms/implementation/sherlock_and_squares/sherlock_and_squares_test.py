import unittest, sherlock_and_squares


class TestSherlockAndSquares(unittest.TestCase):
  def test_sherlock_and_squares(self):
    self.assertEqual(sherlock_and_squares.sherlock_and_squares(3, 9), 2)
    self.assertEqual(sherlock_and_squares.sherlock_and_squares(17, 24), 0)


if __name__ == '__main__':
  unittest.main()
