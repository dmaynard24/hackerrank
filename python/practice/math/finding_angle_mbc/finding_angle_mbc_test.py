import unittest, finding_angle_mbc


class TestFindingAngleMbc(unittest.TestCase):
  def test_finding_angle_mbc(self):
    self.assertEqual(finding_angle_mbc.finding_angle_mbc(10, 10), '45°')


if __name__ == '__main__':
  unittest.main()
