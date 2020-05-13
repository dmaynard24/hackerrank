import unittest, flatland_space_stations


class TestFlatlandSpaceStations(unittest.TestCase):
  def test_flatland_space_stations(self):
    self.assertEqual(
        flatland_space_stations.flatland_space_stations(5, [0, 4]), 2)
    self.assertEqual(
        flatland_space_stations.flatland_space_stations(6, [0, 1, 2, 3, 4, 5]),
        0)
    self.assertEqual(
        flatland_space_stations.flatland_space_stations(
            20, [13, 1, 11, 10, 6]), 6)


if __name__ == '__main__':
  unittest.main()
