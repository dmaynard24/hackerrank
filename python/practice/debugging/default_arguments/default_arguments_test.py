from io import StringIO
from unittest.mock import patch
import unittest, default_arguments


class TestDefaultArguments(unittest.TestCase):
  def test_default_arguments(self):
    with patch('sys.stdout', new=StringIO()) as fake_out:
      default_arguments.default_arguments(['odd 2', 'even 3', 'odd 5'])
      self.assertEqual(fake_out.getvalue(), '''1
3
0
2
4
1
3
5
7
9
''')


if __name__ == '__main__':
  unittest.main()
