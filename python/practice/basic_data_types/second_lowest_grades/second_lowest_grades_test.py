import unittest, second_lowest_grades


class TestSecondLowestGrades(unittest.TestCase):
  def test_second_lowest_grades(self):
    self.assertEqual(
        second_lowest_grades.second_lowest_grades([['Harry', 37.21],
                                                   ['Berry', 37.21],
                                                   ['Tina', 37.2],
                                                   ['Akriti', 41],
                                                   ['Harsh', 39]]),
        ['Berry', 'Harry'])


if __name__ == '__main__':
  unittest.main()
