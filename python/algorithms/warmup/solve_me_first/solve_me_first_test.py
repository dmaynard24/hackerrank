import unittest, solve_me_first


class TestSolveMeFirst(unittest.TestCase):
  def test_solve_me_first(self):
    self.assertEqual(solve_me_first.solve_me_first(2, 3), 5)


if __name__ == '__main__':
  unittest.main()
