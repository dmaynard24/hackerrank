import unittest, ice_cream_parlor


class TestIceCreamParlor(unittest.TestCase):
  def test_ice_cream_parlor(self):
    self.assertEqual(ice_cream_parlor.ice_cream_parlor([1, 4, 5, 3, 2], 4),
                     '1 4')
    self.assertEqual(ice_cream_parlor.ice_cream_parlor([2, 2, 4, 3], 4), '1 2')


if __name__ == '__main__':
  unittest.main()
