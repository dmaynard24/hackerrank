import unittest, very_big_sum


class TestVeryBigSum(unittest.TestCase):
  def test_very_big_sum(self):
    self.assertEqual(
        very_big_sum.very_big_sum([
            1_000_000_001, 1_000_000_002, 1_000_000_003, 1_000_000_004,
            1_000_000_005
        ]), 5_000_000_015)


if __name__ == '__main__':
  unittest.main()
