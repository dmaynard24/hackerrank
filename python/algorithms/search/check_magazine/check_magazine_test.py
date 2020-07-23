import unittest, check_magazine


class TestCheckMagazine(unittest.TestCase):
  def test_check_magazine(self):
    self.assertEqual(
        check_magazine.check_magazine(
            ['give', 'me', 'one', 'grand', 'today', 'night'],
            ['give', 'one', 'grand', 'today']), 'Yes')

  def test_check_magazine_1(self):
    self.assertEqual(
        check_magazine.check_magazine(
            ['two', 'times', 'three', 'is', 'not', 'four'],
            ['two', 'times', 'two', 'is', 'four']), 'No')


if __name__ == '__main__':
  unittest.main()
