import unittest, sock_merchant


class TestSockMerchant(unittest.TestCase):
  def test_sock_merchant(self):
    self.assertEqual(sock_merchant.sock_merchant(7, [1, 2, 1, 2, 1, 3, 2]), 2)
    self.assertEqual(
        sock_merchant.sock_merchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]),
        3)


if __name__ == '__main__':
  unittest.main()
