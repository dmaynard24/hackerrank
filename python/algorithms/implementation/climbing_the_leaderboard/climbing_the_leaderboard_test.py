import unittest, climbing_the_leaderboard


class TestClimbingTheLeaderboard(unittest.TestCase):
  def test_climbing_the_leaderboard(self):
    self.assertEqual(
        climbing_the_leaderboard.climbing_the_leaderboard(
            [100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]), [6, 4, 2, 1])
    self.assertEqual(
        climbing_the_leaderboard.climbing_the_leaderboard(
            [100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102]), [6, 5, 4, 2, 1])


if __name__ == '__main__':
  unittest.main()
