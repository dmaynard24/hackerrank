import unittest, frequency_query


class TestFrequencyQuery(unittest.TestCase):
  def test_frequency_query(self):
    self.assertEqual(
        frequency_query.frequency_query([
            [1, 1],
            [2, 2],
            [3, 2],
            [1, 1],
            [1, 1],
            [2, 1],
            [3, 2],
        ]), [0, 1])

  def test_frequency_query_1(self):
    self.assertEqual(
        frequency_query.frequency_query([[1, 5], [1, 6], [3, 2], [1, 10],
                                         [1, 10], [1, 6], [2, 5], [3, 2]]),
        [0, 1])

  def test_frequency_query_2(self):
    self.assertEqual(
        frequency_query.frequency_query([[1, 3], [2, 3], [3, 2], [1,
                                                                  4], [1, 5],
                                         [1, 5], [1, 4], [3, 2], [2, 4],
                                         [3, 2]]), [0, 1, 1])


if __name__ == '__main__':
  unittest.main()
