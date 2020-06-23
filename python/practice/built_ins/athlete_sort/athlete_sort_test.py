import unittest, athlete_sort


class TestAthleteSort(unittest.TestCase):
  def test_athlete_sort(self):
    self.assertEqual(
        athlete_sort.athlete_sort(
            [[10, 2, 5], [7, 1, 0], [9, 9, 9], [1, 23, 12], [6, 5, 9]], 1),
        '''7 1 0
10 2 5
6 5 9
9 9 9
1 23 12''')


if __name__ == '__main__':
  unittest.main()
