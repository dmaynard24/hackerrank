import unittest, game_of_thrones


class TestGameOfThrones(unittest.TestCase):
  def test_game_of_thrones(self):
    self.assertEqual(game_of_thrones.game_of_thrones('aaabbbb'), 'YES')
    self.assertEqual(game_of_thrones.game_of_thrones('cdefghmnopqrstuvw'),
                     'NO')
    self.assertEqual(game_of_thrones.game_of_thrones('cdcdcdcdeeeef'), 'YES')
    self.assertEqual(game_of_thrones.game_of_thrones('a'), 'YES')


if __name__ == '__main__':
  unittest.main()
