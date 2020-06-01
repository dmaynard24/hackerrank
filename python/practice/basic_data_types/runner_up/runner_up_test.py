import unittest, runner_up


class TestRunnerUp(unittest.TestCase):
  def test_runner_up(self):
    self.assertEqual(runner_up.runner_up([2, 3, 6, 6, 5]), 5)


if __name__ == '__main__':
  unittest.main()
