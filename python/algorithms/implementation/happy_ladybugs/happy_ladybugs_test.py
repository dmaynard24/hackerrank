import unittest, happy_ladybugs


class TestHappyLadybugs(unittest.TestCase):
  def test_happy_ladybugs(self):
    self.assertEqual(happy_ladybugs.happy_ladybugs('RBY_YBR'), 'YES')
    self.assertEqual(happy_ladybugs.happy_ladybugs('X_Y__X'), 'NO')
    self.assertEqual(happy_ladybugs.happy_ladybugs('__'), 'YES')
    self.assertEqual(happy_ladybugs.happy_ladybugs('B_RRBR'), 'YES')


if __name__ == '__main__':
  unittest.main()
