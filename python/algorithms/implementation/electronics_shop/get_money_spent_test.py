import unittest, get_money_spent


class TestGetMoneySpent(unittest.TestCase):
  def test_get_money_spent(self):
    self.assertEqual(get_money_spent.get_money_spent([3, 1], [5, 2, 8], 10), 9)
    self.assertEqual(get_money_spent.get_money_spent([5], [4], 5), -1)


if __name__ == '__main__':
  unittest.main()
