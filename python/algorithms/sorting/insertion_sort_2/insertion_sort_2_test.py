import unittest, insertion_sort_2


class TestInsertionSort2(unittest.TestCase):
  def test_insertion_sort_2(self):
    self.assertEqual(insertion_sort_2.insertion_sort_2(6, [1, 4, 3, 5, 6, 2]),
                     [
                         '1 4 3 5 6 2', '1 3 4 5 6 2', '1 3 4 5 6 2',
                         '1 3 4 5 6 2', '1 2 3 4 5 6'
                     ])


if __name__ == '__main__':
  unittest.main()
