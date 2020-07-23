import unittest, greedy_florist


class TestGreedyFlorist(unittest.TestCase):
  def test_greedy_florist(self):
    self.assertEqual(greedy_florist.get_minimum_cost(2, [2, 5, 6]), 15)

  def test_greedy_florist_1(self):
    self.assertEqual(greedy_florist.get_minimum_cost(3, [1, 3, 5, 7, 9]), 29)


if __name__ == '__main__':
  unittest.main()
