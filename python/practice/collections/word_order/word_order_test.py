from io import StringIO
from unittest.mock import patch
import unittest, word_order


class TestWordOrder(unittest.TestCase):
  def test_word_order(self):
    with patch('sys.stdout', new=StringIO()) as fake_out:
      word_order.word_order(['bcdef', 'abcdefg', 'bcde', 'bcdef'])
      self.assertEqual(fake_out.getvalue(), '''3
2 1 1
''')


if __name__ == '__main__':
  unittest.main()
