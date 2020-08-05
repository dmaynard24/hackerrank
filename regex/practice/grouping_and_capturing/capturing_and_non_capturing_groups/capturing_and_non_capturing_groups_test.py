import unittest, capturing_and_non_capturing_groups


class TestCapturingAndNonCapturingGroups(unittest.TestCase):
  def capturing_and_non_capturing_groups(self):
    self.assertEqual(
        capturing_and_non_capturing_groups.capturing_and_non_capturing_groups(
            'okokok! cya'), 'true')


if __name__ == '__main__':
  unittest.main()
