import unittest, dot_and_cross


class TestDotAndCross(unittest.TestCase):
  def test_dot_and_cross(self):
    self.assertEqual(
        dot_and_cross.dot_and_cross([[1, 2], [3, 4]], [[1, 2], [3, 4]]),
        '''[[ 7 10]
 [15 22]]''')


if __name__ == '__main__':
  unittest.main()