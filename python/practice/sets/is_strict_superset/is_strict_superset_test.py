import unittest, is_strict_superset


class TestIsStrictSuperset(unittest.TestCase):
  def test_is_strict_superset(self):
    self.assertEqual(
        is_strict_superset.is_strict_superset(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 23, 45, 84, 78],
            [[1, 2, 3, 4, 5], [100, 11, 12]]), False)


if __name__ == '__main__':
  unittest.main()
