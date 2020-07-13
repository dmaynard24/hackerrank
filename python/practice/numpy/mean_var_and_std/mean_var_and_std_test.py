from io import StringIO
from unittest.mock import patch
import unittest, mean_var_and_std


class TestMeanVarAndStd(unittest.TestCase):
  def test_mean_var_and_std(self):
    with patch('sys.stdout', new=StringIO()) as fake_out:
      mean_var_and_std.mean_var_and_std([[1, 2], [3, 4]])
      self.assertEqual(fake_out.getvalue(), '''[1.5 3.5]
[1. 1.]
1.118033988749895
''')


if __name__ == '__main__':
  unittest.main()
