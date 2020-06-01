import unittest, is_leap


class TestIsLeap(unittest.TestCase):
  def test_is_leap(self):
    self.assertEqual(is_leap.is_leap(1990), False)
    self.assertEqual(is_leap.is_leap(1996), True)


if __name__ == '__main__':
  unittest.main()
