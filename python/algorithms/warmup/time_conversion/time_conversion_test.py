import unittest, time_conversion


class TestTimeConversion(unittest.TestCase):
  def test_time_conversion(self):
    self.assertEqual(time_conversion.time_conversion('07:05:45PM'), '19:05:45')
    self.assertEqual(time_conversion.time_conversion('12:40:22AM'), '00:40:22')
    self.assertEqual(time_conversion.time_conversion('06:40:03AM'), '06:40:03')
    self.assertEqual(time_conversion.time_conversion('12:40:22PM'), '12:40:22')


if __name__ == '__main__':
  unittest.main()
