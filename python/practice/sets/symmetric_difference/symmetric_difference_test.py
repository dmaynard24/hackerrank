import unittest, symmetric_difference


class TestSymmetricDifference(unittest.TestCase):
  def test_symmetric_difference(self):
    self.assertEqual(
        symmetric_difference.symmetric_difference([2, 4, 5, 9],
                                                  [2, 4, 11, 12]), '''5
9
11
12''')


if __name__ == '__main__':
  unittest.main()
