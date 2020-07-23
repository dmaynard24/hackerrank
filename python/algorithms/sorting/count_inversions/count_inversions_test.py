import unittest, count_inversions


class TestCountInversions(unittest.TestCase):
  def test_count_inversions(self):
    self.assertEqual(count_inversions.count_inversions([1, 1, 1, 2, 2]), 0)

  def test_count_inversions_1(self):
    self.assertEqual(count_inversions.count_inversions([2, 1, 3, 1, 2]), 4)

  def test_count_inversions_2(self):
    self.assertEqual(count_inversions.count_inversions([7, 5, 3, 1]), 6)

  def test_count_inversions_3(self):
    self.assertEqual(count_inversions.count_inversions([3, 2, 1]), 3)


if __name__ == '__main__':
  unittest.main()
