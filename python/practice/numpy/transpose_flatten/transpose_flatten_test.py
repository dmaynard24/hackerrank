from io import StringIO
from unittest.mock import patch
import unittest, transpose_flatten


class TestTransposeFlatten(unittest.TestCase):
  def test_transpose_flatten(self):
    with patch('sys.stdout', new=StringIO()) as fake_out:
      transpose_flatten.transpose_flatten([[1, 2], [3, 4]])
      self.assertEqual(fake_out.getvalue(), '''[[1 3]
 [2 4]]
[1 2 3 4]
''')


if __name__ == '__main__':
  unittest.main()
