import unittest, icecream_parlor


class TestIceCreamParlor(unittest.TestCase):
  def test_icecream_parlor(self):
    self.assertEqual(icecream_parlor.icecream_parlor(4, [1, 4, 5, 3, 2]),
                     [1, 4])

  def test_icecream_parlor_1(self):
    self.assertEqual(icecream_parlor.icecream_parlor(4, [2, 2, 4, 3]), [1, 2])


if __name__ == '__main__':
  unittest.main()
