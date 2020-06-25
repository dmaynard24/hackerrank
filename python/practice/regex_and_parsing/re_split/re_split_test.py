import unittest, re_split


class TestReSplit(unittest.TestCase):
  def test_re_split(self):
    self.assertEqual(re_split.re_split('100,000,000.000'), '''100
000
000
000''')


if __name__ == '__main__':
  unittest.main()
