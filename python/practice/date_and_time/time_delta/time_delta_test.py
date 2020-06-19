import unittest, time_delta


class TestTimeDelta(unittest.TestCase):
  def test_time_delta(self):
    self.assertEqual(
        time_delta.time_delta('Sun 10 May 2015 13:54:36 -0700',
                              'Sun 10 May 2015 13:54:36 -0000'), '25200')


if __name__ == '__main__':
  unittest.main()
