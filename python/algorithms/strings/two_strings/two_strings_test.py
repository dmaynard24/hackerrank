import unittest, two_strings


class TestTwoStrings(unittest.TestCase):
  def test_two_strings(self):
    self.assertEqual(two_strings.two_strings('hello', 'world'), 'YES')

  def test_two_strings_1(self):
    self.assertEqual(two_strings.two_strings('hi', 'world'), 'NO')


if __name__ == '__main__':
  unittest.main()
