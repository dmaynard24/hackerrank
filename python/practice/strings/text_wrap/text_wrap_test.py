import unittest, text_wrap


class TestTextWrap(unittest.TestCase):
  def test_text_wrap(self):
    self.assertEqual(text_wrap.text_wrap('ABCDEFGHIJKLIMNOQRSTUVWXYZ', 4),
                     '''ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ''')


if __name__ == '__main__':
  unittest.main()
