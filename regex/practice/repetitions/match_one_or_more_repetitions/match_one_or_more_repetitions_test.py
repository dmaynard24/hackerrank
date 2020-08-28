import unittest, match_one_or_more_repetitions


class TestMatchOneOrMoreRepetitions(unittest.TestCase):
  def test_match_one_or_more_repetitions(self):
    self.assertEqual(
        match_one_or_more_repetitions.match_one_or_more_repetitions('1Qa'),
        'true')

  def test_match_one_or_more_repetitions_1(self):
    self.assertEqual(
        match_one_or_more_repetitions.match_one_or_more_repetitions('qQa'),
        'false')


if __name__ == '__main__':
  unittest.main()
