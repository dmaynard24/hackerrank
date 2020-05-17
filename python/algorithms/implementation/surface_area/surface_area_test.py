import unittest, surface_area


class TestSurfaceArea(unittest.TestCase):
  def test_surface_area(self):
    self.assertEqual(surface_area.surface_area([[1]]), 6)
    self.assertEqual(
        surface_area.surface_area([[1, 3, 4], [2, 2, 3], [1, 2, 4]]), 60)


if __name__ == '__main__':
  unittest.main()
