import unittest, calendar_module


class TestCalendarModule(unittest.TestCase):
  def test_calendar_module(self):
    self.assertEqual(calendar_module.day_name('08 05 2015'), 'WEDNESDAY')


if __name__ == '__main__':
  unittest.main()
