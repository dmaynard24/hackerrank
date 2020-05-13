import unittest, cavity_map


class TestCavityMap(unittest.TestCase):
  def test_cavity_map(self):
    self.assertEqual(cavity_map.cavity_map(['1112', '1912', '1892', '1234']),
                     ['1112', '1X12', '18X2', '1234'])


if __name__ == '__main__':
  unittest.main()
