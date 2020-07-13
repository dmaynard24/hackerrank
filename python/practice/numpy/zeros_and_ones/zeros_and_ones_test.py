from io import StringIO
from unittest.mock import patch
import unittest, zeros_and_ones


class TestZerosAndOnes(unittest.TestCase):
  def test_zeros_and_ones(self):
    with patch('sys.stdout', new=StringIO()) as fake_out:
      zeros_and_ones.zeros_and_ones((3, 3, 3))
      self.assertEqual(
          fake_out.getvalue(), '''[[[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]]
[[[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]]
''')


if __name__ == '__main__':
  unittest.main()
