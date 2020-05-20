import unittest, weighted_uniform_strings


class TestWeightedUniformStrings(unittest.TestCase):
  def test_weighted_uniform_strings(self):
    self.assertEqual(
        weighted_uniform_strings.weighted_uniform_strings(
            'abccddde', [1, 3, 12, 5, 9, 10]),
        ['Yes', 'Yes', 'Yes', 'Yes', 'No', 'No'])
    self.assertEqual(
        weighted_uniform_strings.weighted_uniform_strings(
            'aaabbbbcccddd', [9, 7, 8, 12, 5]),
        ['Yes', 'No', 'Yes', 'Yes', 'No'])


if __name__ == '__main__':
  unittest.main()
