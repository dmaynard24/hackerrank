import unittest, count_triplets


class TestCountTriplets(unittest.TestCase):
  def test_count_triplets(self):
    self.assertEqual(count_triplets.count_triplets([1, 2, 2, 4], 2), 2)

  def test_count_triplets_1(self):
    self.assertEqual(count_triplets.count_triplets([1, 3, 9, 9, 27, 81], 3), 6)

  def test_count_triplets_2(self):
    self.assertEqual(count_triplets.count_triplets([1, 5, 5, 25, 125], 5), 4)

  def test_count_triplets_3(self):
    self.assertEqual(
        count_triplets.count_triplets([
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
        ], 1), 161_700)


if __name__ == '__main__':
  unittest.main()
