import unittest, minimum_bribes


class TestMinimumBribes(unittest.TestCase):
  def test_minimum_bribes(self):
    self.assertEqual(minimum_bribes.minimum_bribes([2, 1, 5, 3, 4]), 3)

  def test_minimum_bribes_1(self):
    self.assertEqual(minimum_bribes.minimum_bribes([2, 5, 1, 3, 4]),
                     'Too chaotic')

  def test_minimum_bribes_2(self):
    self.assertEqual(minimum_bribes.minimum_bribes([1, 2, 5, 3, 4, 7, 8, 6]),
                     4)

  def test_minimum_bribes_3(self):
    self.assertEqual(minimum_bribes.minimum_bribes([1, 2, 5, 3, 7, 8, 6, 4]),
                     7)


if __name__ == '__main__':
  unittest.main()
