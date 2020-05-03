import unittest, hurdle_race


class TestHurdleRace(unittest.TestCase):
  def test_hurdle_race(self):
    self.assertEqual(hurdle_race.hurdle_race(4, [1, 6, 3, 5, 2]), 2)
    self.assertEqual(hurdle_race.hurdle_race(7, [2, 5, 4, 5, 2]), 0)


if __name__ == '__main__':
  unittest.main()
