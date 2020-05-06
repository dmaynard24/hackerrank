import unittest, extra_long_factorials


class TestFindDigits(unittest.TestCase):
  def test_extra_long_factorials(self):
    self.assertEqual(extra_long_factorials.extra_long_factorials(25),
                     15_511_210_043_330_985_984_000_000)
    self.assertEqual(
        extra_long_factorials.extra_long_factorials(45),
        119_622_220_865_480_194_561_963_161_495_657_715_064_383_733_760_000_000_000
    )


if __name__ == '__main__':
  unittest.main()