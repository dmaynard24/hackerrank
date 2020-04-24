import unittest, compare_triplets


class TestCompareTriplets(unittest.TestCase):
  def test_compare_triplets(self):
    self.assertEqual(compare_triplets.compare_triplets([5, 6, 7], [3, 6, 10]),
                     [1, 1])
    self.assertEqual(
        compare_triplets.compare_triplets([17, 28, 30], [99, 16, 8]), [2, 1])


if __name__ == '__main__':
  unittest.main()
