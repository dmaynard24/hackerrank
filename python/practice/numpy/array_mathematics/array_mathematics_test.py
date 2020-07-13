from io import StringIO
from unittest.mock import patch
import unittest, array_mathematics


class TestArrayMathematics(unittest.TestCase):
  def test_array_mathematics(self):
    with patch('sys.stdout', new=StringIO()) as fake_out:
      array_mathematics.array_mathematics([1, 2, 3, 4], [5, 6, 7, 8])
      self.assertEqual(
          fake_out.getvalue(), '''[[ 6  8 10 12]]
[[-4 -4 -4 -4]]
[[ 5 12 21 32]]
[[0 0 0 0]]
[[1 2 3 4]]
[[    1    64  2187 65536]]
''')


if __name__ == '__main__':
  unittest.main()
