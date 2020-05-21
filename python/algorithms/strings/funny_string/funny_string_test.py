import unittest, funny_string


class TestFunnyString(unittest.TestCase):
  def test_funny_string(self):
    self.assertEqual(funny_string.funny_string('acxz'), 'Funny')
    self.assertEqual(funny_string.funny_string('bcxz'), 'Not Funny')
    self.assertEqual(funny_string.funny_string('ivvkxq'), 'Not Funny')
    self.assertEqual(funny_string.funny_string('ivvkx'), 'Not Funny')


if __name__ == '__main__':
  unittest.main()
