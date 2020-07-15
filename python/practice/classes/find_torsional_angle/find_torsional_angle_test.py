import unittest, find_torsional_angle


class TestFindTorsionalAngle(unittest.TestCase):
  def test_find_torsional_angle(self):
    self.assertEqual(
        find_torsional_angle.find_torsional_angle([[0, 4, 5], [1, 7, 6],
                                                   [0, 5, 9], [1, 7, 2]]),
        8.19)


if __name__ == '__main__':
  unittest.main()
