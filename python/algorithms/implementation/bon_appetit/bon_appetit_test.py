import unittest, bon_appetit


class TestDayOfTheProgrammer(unittest.TestCase):
  def test_bon_appetit(self):
    self.assertEqual(bon_appetit.bon_appetit([3, 10, 2, 9], 1, 12), 5)
    self.assertEqual(bon_appetit.bon_appetit([3, 10, 2, 9], 1, 7),
                     'Bon Appetit')


if __name__ == '__main__':
  unittest.main()
