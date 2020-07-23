import unittest, max_min


class TestMaxMin(unittest.TestCase):
  def test_max_min(self):
    self.assertEqual(max_min.max_min(3, [10, 100, 300, 200, 1_000, 20, 30]),
                     20)

  def test_max_min(self):
    self.assertEqual(
        max_min.max_min(4, [1, 2, 3, 4, 10, 20, 30, 40, 100, 200]), 3)

  def test_max_min(self):
    self.assertEqual(max_min.max_min(2, [1, 2, 1, 2, 1]), 0)


if __name__ == '__main__':
  unittest.main()
