import unittest, backreferences_to_failed_groups


class TestBackreferencesToFailedGroups(unittest.TestCase):
  def test_backreferences_to_failed_groups(self):
    self.assertEqual(
        backreferences_to_failed_groups.backreferences_to_failed_groups(
            '12-34-56-78'), 'true')


if __name__ == '__main__':
  unittest.main()
