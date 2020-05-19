import unittest, fair_rations


class TestFairRations(unittest.TestCase):
  def test_fair_rations(self):
    self.assertEqual(fair_rations.fair_rations([2, 3, 4, 5, 6]), 4)
    self.assertEqual(fair_rations.fair_rations([1, 2]), 'NO')


if __name__ == '__main__':
  unittest.main()
