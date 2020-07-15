from io import StringIO
from unittest.mock import patch
import unittest, mod_divmod


class TestModDivmod(unittest.TestCase):
  def test_mod_divmod(self):
    with patch('sys.stdout', new=StringIO()) as fake_out:
      mod_divmod.mod_divmod(177, 10)
      self.assertEqual(fake_out.getvalue(), '''17
7
(17, 7)
''')


if __name__ == '__main__':
  unittest.main()
