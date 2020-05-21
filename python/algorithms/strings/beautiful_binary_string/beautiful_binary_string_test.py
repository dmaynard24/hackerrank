import unittest, beautiful_binary_string


class TestBeautifulBinaryString(unittest.TestCase):
  def test_beautiful_binary_string(self):
    self.assertEqual(
        beautiful_binary_string.beautiful_binary_string('0101010'), 2)
    self.assertEqual(beautiful_binary_string.beautiful_binary_string('01100'),
                     0)
    self.assertEqual(
        beautiful_binary_string.beautiful_binary_string('0100101010'), 3)


if __name__ == '__main__':
  unittest.main()
