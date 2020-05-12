import unittest, beautiful_triplets


class TestBeautifulTriplets(unittest.TestCase):
  def test_beautiful_triplets(self):
    self.assertEqual(
        beautiful_triplets.beautiful_triplets(3, [1, 2, 4, 5, 7, 8, 10]), 3)
    self.assertEqual(
        beautiful_triplets.beautiful_triplets(
            3, [1, 6, 7, 7, 8, 10, 12, 13, 14, 19]), 2)


if __name__ == '__main__':
  unittest.main()
