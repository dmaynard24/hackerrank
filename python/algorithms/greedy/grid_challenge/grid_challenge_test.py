import unittest, grid_challenge


class TestGridChallenge(unittest.TestCase):
  def test_grid_challenge(self):
    self.assertEqual(
        grid_challenge.grid_challenge(
            ['eabcd', 'fghij', 'olkmn', 'trpqs', 'xywuv']), 'YES')
    self.assertEqual(grid_challenge.grid_challenge(['mpxz', 'abcd', 'wlmf']),
                     'NO')


if __name__ == '__main__':
  unittest.main()
