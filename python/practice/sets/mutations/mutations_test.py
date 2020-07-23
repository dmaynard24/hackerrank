import unittest, mutations


class TestMutations(unittest.TestCase):
  def test_mutations(self):
    self.assertEqual(
        mutations.mutations(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 24, 52],
            [['intersection_update 10', [2, 3, 5, 6, 8, 9, 1, 4, 7, 11]],
             ['update 2', [55, 66]],
             ['symmetric_difference_update 5', [22, 7, 35, 62, 58]],
             ['difference_update 7', [11, 22, 35, 55, 58, 62, 66]]]), 38)


if __name__ == '__main__':
  unittest.main()
