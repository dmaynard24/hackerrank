import unittest, re_group


class TestReGroup(unittest.TestCase):
  def test_re_group(self):
    self.assertEqual(re_group.re_group('12345678910111213141516171820212223'),
                     '1')
    self.assertEqual(re_group.re_group('__commit__'), 'm')
    self.assertEqual(re_group.re_group('__comit__'), '-1')


if __name__ == '__main__':
  unittest.main()
