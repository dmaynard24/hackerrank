import unittest, sorting_comparator


class TestSortingComparator(unittest.TestCase):
  def test_sorting_comparator(self):
    self.assertEqual(
        sorting_comparator.sorting_comparator([
            'amy 100', 'david 100', 'heraldo 50', 'aakansha 75', 'aleksa 150'
        ]), '''aleksa 150
amy 100
david 100
aakansha 75
heraldo 50''')


if __name__ == '__main__':
  unittest.main()
