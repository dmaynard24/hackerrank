import unittest, piling_up


class TestPilingUp(unittest.TestCase):
  def test_piling_up(self):
    self.assertEqual(piling_up.is_valid_pile([4, 3, 2, 1, 3, 4]), True)

  def test_piling_up_1(self):
    self.assertEqual(piling_up.is_valid_pile([1, 3, 2]), False)


if __name__ == '__main__':
  unittest.main()