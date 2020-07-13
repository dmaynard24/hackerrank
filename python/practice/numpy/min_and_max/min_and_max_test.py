import unittest, min_and_max


class TestMinAndMax(unittest.TestCase):
  def test_min_and_max(self):
    self.assertEqual(min_and_max.min_and_max([[2, 5], [3, 7], [1, 3], [4, 0]]),
                     3)


if __name__ == '__main__':
  unittest.main()