import unittest, viral_advertising


class TestViralAdvertising(unittest.TestCase):
  def test_viral_advertising(self):
    self.assertEqual(viral_advertising.viral_advertising(3), 9)
    self.assertEqual(viral_advertising.viral_advertising(5), 24)


if __name__ == '__main__':
  unittest.main()
