import unittest, product


class TestProduct(unittest.TestCase):
  def test_product(self):
    self.assertEqual(product.product([1, 2], [3, 4]),
                     '(1, 3) (1, 4) (2, 3) (2, 4)')


if __name__ == '__main__':
  unittest.main()
