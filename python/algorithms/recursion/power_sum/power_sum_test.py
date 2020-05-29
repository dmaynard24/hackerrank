import unittest, power_sum


class TestPowerSum(unittest.TestCase):
  def test_power_sum(self):
    self.assertEqual(power_sum.power_sum(100, 2), 3)
    self.assertEqual(power_sum.power_sum(10, 2), 1)
    self.assertEqual(power_sum.power_sum(100, 3), 1)


if __name__ == '__main__':
  unittest.main()
