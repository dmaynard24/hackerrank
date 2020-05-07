import unittest, cut_the_sticks


class TestCutTheSticks(unittest.TestCase):
  def test_cut_the_sticks(self):
    self.assertEqual(cut_the_sticks.cut_the_sticks([5, 4, 4, 2, 2, 8]),
                     [6, 4, 2, 1])
    self.assertEqual(cut_the_sticks.cut_the_sticks([1, 2, 3, 4, 3, 3, 2, 1]),
                     [8, 6, 4, 1])


if __name__ == '__main__':
  unittest.main()
