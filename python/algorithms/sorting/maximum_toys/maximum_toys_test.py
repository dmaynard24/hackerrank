import unittest, maximum_toys


class TestMaximumToys(unittest.TestCase):
  def test_maximum_toys(self):
    self.assertEqual(
        maximum_toys.maximum_toys([1, 12, 5, 111, 200, 1000, 10], 50), 4)


if __name__ == '__main__':
  unittest.main()
