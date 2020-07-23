import unittest, luck_balance


class TestLuckBalance(unittest.TestCase):
  def test_luck_balance(self):
    self.assertEqual(
        luck_balance.luck_balance(
            3, [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]), 29)


if __name__ == '__main__':
  unittest.main()
