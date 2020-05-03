import unittest, beautiful_days


class TestBeautifulDays(unittest.TestCase):
  def test_beautiful_days(self):
    self.assertEqual(beautiful_days.beautiful_days(20, 23, 6), 2)
    self.assertEqual(beautiful_days.beautiful_days(13, 45, 3), 33)


if __name__ == '__main__':
  unittest.main()
