import unittest, service_lane


class TestServiceLane(unittest.TestCase):
  def test_service_lane(self):
    self.assertEqual(
        service_lane.service_lane([2, 3, 1, 2, 3, 2, 3, 3],
                                  [[0, 3], [4, 6], [6, 7], [3, 5], [0, 7]]),
        [1, 2, 3, 2, 1])


if __name__ == '__main__':
  unittest.main()
