import unittest, breaking_records


class TestBreakingRecords(unittest.TestCase):
  def test_breaking_records(self):
    self.assertEqual(
        breaking_records.breaking_records([10, 5, 20, 20, 4, 5, 2, 25, 1]),
        [2, 4])
    self.assertEqual(
        breaking_records.breaking_records(
            [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]), [4, 0])


if __name__ == '__main__':
  unittest.main()
