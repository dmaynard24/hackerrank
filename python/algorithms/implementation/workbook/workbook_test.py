import unittest, workbook


class TestWorkbook(unittest.TestCase):
  def test_workbook(self):
    self.assertEqual(workbook.workbook(5, 3, [4, 2, 6, 1, 10]), 4)
    self.assertEqual(
        workbook.workbook(10, 5, [3, 8, 15, 11, 14, 1, 9, 2, 24, 31]), 8)


if __name__ == '__main__':
  unittest.main()
