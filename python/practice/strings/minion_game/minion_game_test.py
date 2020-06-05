import unittest, minion_game


class TestMinionGame(unittest.TestCase):
  def test_minion_game(self):
    self.assertEqual(minion_game.minion_game('BANANA'), 'Stuart 12')


if __name__ == '__main__':
  unittest.main()
