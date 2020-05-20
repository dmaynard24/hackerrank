import unittest, hackerrank_in_string


class TestHackerrankInString(unittest.TestCase):
  def test_hackerrank_in_string(self):
    self.assertEqual(
        hackerrank_in_string.hackerrank_in_string('hereiamstackerrank'), 'YES')
    self.assertEqual(hackerrank_in_string.hackerrank_in_string('hackerworld'),
                     'NO')
    self.assertEqual(
        hackerrank_in_string.hackerrank_in_string('hhaacckkekraraannk'), 'YES')
    self.assertEqual(
        hackerrank_in_string.hackerrank_in_string(
            'rhbaasdndfsdskgbfefdbrsdfhuyatrjtcrtyytktjjt'), 'NO')


if __name__ == '__main__':
  unittest.main()
