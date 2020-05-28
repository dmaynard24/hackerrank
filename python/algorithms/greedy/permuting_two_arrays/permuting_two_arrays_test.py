import unittest, permuting_two_arrays


class TestPermutingTwoArrays(unittest.TestCase):
  def test_permuting_two_arrays(self):
    self.assertEqual(
        permuting_two_arrays.permuting_two_arrays(10, [2, 1, 3], [7, 8, 9]),
        'YES')
    self.assertEqual(
        permuting_two_arrays.permuting_two_arrays(5, [1, 2, 2, 1],
                                                  [3, 3, 3, 4]), 'NO')


if __name__ == '__main__':
  unittest.main()
