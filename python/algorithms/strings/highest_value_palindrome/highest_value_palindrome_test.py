import unittest, highest_value_palindrome


class TestHighestValuePalindrome(unittest.TestCase):
  def test_highest_value_palindrome(self):
    self.assertEqual(
        highest_value_palindrome.highest_value_palindrome('3943', 4, 1),
        '3993')
    self.assertEqual(
        highest_value_palindrome.highest_value_palindrome('092282', 6, 3),
        '992299')
    self.assertEqual(
        highest_value_palindrome.highest_value_palindrome('0011', 4, 1), '-1')


if __name__ == '__main__':
  unittest.main()
