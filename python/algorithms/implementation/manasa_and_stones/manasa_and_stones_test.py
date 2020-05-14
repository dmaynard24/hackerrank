import unittest, manasa_and_stones


class TestManasaAndStones(unittest.TestCase):
  def test_manasa_and_stones(self):
    self.assertEqual(manasa_and_stones.manasa_and_stones(3, 1, 2), [2, 3, 4])
    self.assertEqual(manasa_and_stones.manasa_and_stones(4, 10, 100),
                     [30, 120, 210, 300])
    self.assertEqual(manasa_and_stones.manasa_and_stones(73, 25, 25), [1_800])
    self.assertEqual(manasa_and_stones.manasa_and_stones(5, 3, 23),
                     [12, 32, 52, 72, 92])


if __name__ == '__main__':
  unittest.main()
