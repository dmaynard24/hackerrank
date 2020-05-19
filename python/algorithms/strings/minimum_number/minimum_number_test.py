import unittest, minimum_number


class TestMinimumNumber(unittest.TestCase):
  def test_minimum_number(self):
    self.assertEqual(minimum_number.minimum_number(3, 'Ab1'), 3)
    self.assertEqual(minimum_number.minimum_number(11, '#HackerRank'), 1)
    self.assertEqual(minimum_number.minimum_number(7, 'AUzs-nV'), 1)


if __name__ == '__main__':
  unittest.main()
