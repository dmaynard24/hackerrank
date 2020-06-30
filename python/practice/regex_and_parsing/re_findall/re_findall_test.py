import unittest, re_findall


class TestReFindall(unittest.TestCase):
  def test_re_findall(self):
    self.assertEqual(re_findall.re_findall('rabcdeefgyYhFjkIoomnpOeorteeeeet'),
                     '''ee
Ioo
Oeo
eeeee''')
    self.assertEqual(re_findall.re_findall('abaabaabaabaae'), '''aa
aa
aa''')


if __name__ == '__main__':
  unittest.main()
