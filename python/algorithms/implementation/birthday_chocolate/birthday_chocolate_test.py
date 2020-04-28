import unittest, birthday_chocolate


class TestBirthdayChocolate(unittest.TestCase):
  def test_birthday_chocolate(self):
    self.assertEqual(
        birthday_chocolate.birthday_chocolate([1, 2, 1, 3, 2], 3, 2), 2)
    self.assertEqual(
        birthday_chocolate.birthday_chocolate([1, 1, 1, 1, 1, 1], 3, 2), 0)
    self.assertEqual(birthday_chocolate.birthday_chocolate([4], 4, 1), 1)


if __name__ == '__main__':
  unittest.main()
