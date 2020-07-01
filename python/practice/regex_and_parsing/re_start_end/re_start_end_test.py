import unittest, re_start_end


class TestReStartEnd(unittest.TestCase):
  def test_re_start_end(self):
    self.assertEqual(re_start_end.re_start_end('aaadaa', 'aa'), '''(0, 1)
(1, 2)
(4, 5)''')
    self.assertEqual(re_start_end.re_start_end('jjhv', 'z'), '(-1, -1)')


if __name__ == '__main__':
  unittest.main()
