import unittest, acm_team


class TestAcmTeam(unittest.TestCase):
  def test_acm_team(self):
    self.assertEqual(acm_team.acm_team(['10101', '11100', '11010', '00101']),
                     [5, 2])
    self.assertEqual(
        acm_team.acm_team(
            ['11101', '10101', '11001', '10111', '10000', '01110']), [5, 6])


if __name__ == '__main__':
  unittest.main()
