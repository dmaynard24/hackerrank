import unittest, grading_students


class TestGradingStudents(unittest.TestCase):
  def test_grading_students(self):
    self.assertEqual(grading_students.grading_students([73, 67, 38, 33]),
                     [75, 67, 40, 33])


if __name__ == '__main__':
  unittest.main()
