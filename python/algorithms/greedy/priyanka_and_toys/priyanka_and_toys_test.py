import unittest, priyanka_and_toys


class TestPriyankaAndToys(unittest.TestCase):
  def test_priyanka_and_toys(self):
    self.assertEqual(
        priyanka_and_toys.priyanka_and_toys([1, 2, 3, 21, 7, 12, 14, 21]), 4)
    self.assertEqual(
        priyanka_and_toys.priyanka_and_toys([12, 15, 7, 8, 19, 24]), 4)


if __name__ == '__main__':
  unittest.main()
