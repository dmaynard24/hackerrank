import unittest, birthday_cake_candles


class TestBirthdayCakeCandles(unittest.TestCase):
  def test_birthday_cake_candles(self):
    self.assertEqual(birthday_cake_candles.birthday_cake_candles([3, 2, 1, 3]),
                     2)


if __name__ == '__main__':
  unittest.main()
