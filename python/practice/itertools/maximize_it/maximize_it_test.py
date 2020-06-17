import unittest, maximize_it


class TestMaximizeIt(unittest.TestCase):
  def test_maximize_it(self):
    self.assertEqual(
        maximize_it.maximize_it(3, 1_000,
                                [[5, 4], [7, 8, 9], [5, 7, 8, 9, 10]]), 206)


if __name__ == '__main__':
  unittest.main()
