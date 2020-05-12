import unittest, halloween_sale


class TestHalloweenSale(unittest.TestCase):
  def test_halloween_sale(self):
    self.assertEqual(halloween_sale.halloween_sale(20, 3, 6, 80), 6)
    self.assertEqual(halloween_sale.halloween_sale(20, 3, 6, 85), 7)


if __name__ == '__main__':
  unittest.main()
