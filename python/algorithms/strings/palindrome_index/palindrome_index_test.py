import unittest, palindrome_index


class TestPalindromeIndex(unittest.TestCase):
  def test_palindrome_index(self):
    self.assertEqual(palindrome_index.palindrome_index('aaab'), 3)
    self.assertEqual(palindrome_index.palindrome_index('baa'), 0)
    self.assertEqual(palindrome_index.palindrome_index('aaa'), -1)
    self.assertEqual(
        palindrome_index.palindrome_index(
            'hgygsvlfcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcwflvsgygh'), 44)


if __name__ == '__main__':
  unittest.main()
