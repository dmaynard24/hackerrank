import unittest, activity_notifications


class TestActivityNotifications(unittest.TestCase):
  def test_activity_notifications(self):
    self.assertEqual(
        activity_notifications.activity_notifications(
            [2, 3, 4, 2, 3, 6, 8, 4, 5], 5), 2)

  def test_activity_notifications_1(self):
    self.assertEqual(
        activity_notifications.activity_notifications([1, 2, 3, 4, 4], 4), 0)

  def test_activity_notifications_2(self):
    self.assertEqual(
        activity_notifications.activity_notifications([10, 20, 30, 40, 50], 3),
        1)


if __name__ == '__main__':
  unittest.main()
