import unittest, incorrect_regex


class TestIncorrectRegex(unittest.TestCase):
  def test_incorrect_regex(self):
    self.assertEqual(incorrect_regex.incorrect_regex('.*\+'), True)
    self.assertEqual(incorrect_regex.incorrect_regex('.*+'), False)


if __name__ == '__main__':
  unittest.main()
