import unittest, quicksort_1


class TestQuicksort1(unittest.TestCase):
  def test_quicksort_1(self):
    self.assertEqual(quicksort_1.quicksort_1([4, 5, 3, 7, 2]), [3, 2, 4, 5, 7])


if __name__ == '__main__':
  unittest.main()
