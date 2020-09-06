import unittest, get_ip_address_type


class TestGetIpAddressType(unittest.TestCase):
  def test_get_ip_address_type(self):
    self.assertEqual(
        get_ip_address_type.get_ip_address_type('This line has junk text.'),
        'Neither')

  def test_get_ip_address_type_1(self):
    self.assertEqual(get_ip_address_type.get_ip_address_type('121.18.19.20'),
                     'IPv4')

  def test_get_ip_address_type_2(self):
    self.assertEqual(
        get_ip_address_type.get_ip_address_type(
            '2001:0db8:0000:0000:0000:ff00:0042:8329'), 'IPv6')


if __name__ == '__main__':
  unittest.main()
