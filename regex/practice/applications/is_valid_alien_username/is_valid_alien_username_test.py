import unittest, is_valid_alien_username


class TestIsValidAlienUsername(unittest.TestCase):
  def test_is_valid_alien_username(self):
    self.assertEqual(
        is_valid_alien_username.is_valid_alien_username('_0898989811abced_'),
        True)

  def test_is_valid_alien_username_1(self):
    self.assertEqual(is_valid_alien_username.is_valid_alien_username('_abce'),
                     False)

  def test_is_valid_alien_username_2(self):
    self.assertEqual(
        is_valid_alien_username.is_valid_alien_username('_09090909abcD0'),
        False)


if __name__ == '__main__':
  unittest.main()
