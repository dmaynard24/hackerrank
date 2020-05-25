import unittest, insertion_sort_1


class TestInsertionSort1(unittest.TestCase):
  def test_insertion_sort_1(self):
    self.assertEqual(insertion_sort_1.insertion_sort_1(5, [2, 4, 6, 8, 3]),
                     ['2 4 6 8 8', '2 4 6 6 8', '2 4 4 6 8', '2 3 4 6 8'])


if __name__ == '__main__':
  unittest.main()
