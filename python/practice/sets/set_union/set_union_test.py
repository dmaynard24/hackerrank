import unittest, set_union


class TestSetUnion(unittest.TestCase):
  def test_set_union(self):
    self.assertEqual(
        set_union.set_union([1, 2, 3, 4, 5, 6, 7, 8, 9],
                            [10, 1, 2, 3, 11, 21, 55, 6, 8]), 13)


if __name__ == '__main__':
  unittest.main()
