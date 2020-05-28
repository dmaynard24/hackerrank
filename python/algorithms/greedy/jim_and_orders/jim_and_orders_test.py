import unittest, jim_and_orders


class TestJimAndOrders(unittest.TestCase):
  def test_jim_and_orders(self):
    self.assertEqual(jim_and_orders.jim_and_orders([
        [1, 3],
        [2, 3],
        [3, 3],
    ]), [1, 2, 3])
    self.assertEqual(
        jim_and_orders.jim_and_orders([[8, 1], [4, 2], [5, 6], [3, 1],
                                       [4, 3]]), [4, 2, 5, 1, 3])


if __name__ == '__main__':
  unittest.main()
