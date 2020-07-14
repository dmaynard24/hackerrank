from io import StringIO
from unittest.mock import patch
import unittest, inner_and_outer


class TestInnerAndOuter(unittest.TestCase):
  def test_inner_and_outer(self):
    with patch('sys.stdout', new=StringIO()) as fake_out:
      inner_and_outer.inner_and_outer([0, 1], [2, 3])
      self.assertEqual(fake_out.getvalue(), '''3
[[0 0]
 [2 3]]
''')


if __name__ == '__main__':
  unittest.main()
