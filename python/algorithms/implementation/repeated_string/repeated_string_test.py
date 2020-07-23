import unittest, repeated_string


class TestRepeatedString(unittest.TestCase):
  def test_repeated_string(self):
    self.assertEqual(repeated_string.repeated_string('aba', 10), 7)

  def test_repeated_string_1(self):
    self.assertEqual(repeated_string.repeated_string('a', 1000000000000),
                     1000000000000)


if __name__ == '__main__':
  unittest.main()
