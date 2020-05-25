import unittest, running_time


class TestRunningTime(unittest.TestCase):
  def test_running_time(self):
    self.assertEqual(running_time.running_time([2, 1, 3, 1, 2]), 4)
    self.assertEqual(
        running_time.running_time([1, 1, 2, 2, 3, 3, 5, 5, 7, 7, 9, 9]), 0)


if __name__ == '__main__':
  unittest.main()
