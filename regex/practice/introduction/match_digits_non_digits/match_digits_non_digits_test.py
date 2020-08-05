import unittest, match_digits_non_digits


class TestMatchDigitsNonDigits(unittest.TestCase):
  def test_match_digits_non_digits(self):
    self.assertEqual(
        match_digits_non_digits.match_digits_non_digits('06-11-2015'), 'true')


if __name__ == '__main__':
  unittest.main()
