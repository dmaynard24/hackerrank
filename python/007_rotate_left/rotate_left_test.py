import unittest, rotate_left


class TestRotateLeft(unittest.TestCase):
  def test_rotate_left(self):
    self.assertEqual(rotate_left.rotate_left([1, 2, 3, 4, 5], 2),
                     [3, 4, 5, 1, 2])
    self.assertEqual(rotate_left.rotate_left([1, 2, 3, 4, 5], 4),
                     [5, 1, 2, 3, 4])


if __name__ == '__main__':
  unittest.main()
