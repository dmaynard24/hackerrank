import unittest, get_total_x


class TestGetTotalX(unittest.TestCase):
  def test_get_total_x(self):
    self.assertEqual(get_total_x.get_total_x([2, 6], [24, 36]), 2)
    self.assertEqual(get_total_x.get_total_x([3, 4], [24, 48]), 2)
    self.assertEqual(get_total_x.get_total_x([2, 4], [16, 32, 96]), 3)


if __name__ == '__main__':
  unittest.main()
