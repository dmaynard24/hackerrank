import unittest, match_zero_or_more_repetitions


class TestMatchZeroOrMoreRepetitions(unittest.TestCase):
  def match_zero_or_more_repetitions(self):
    self.assertEqual(
        match_zero_or_more_repetitions.match_zero_or_more_repetitions('14'),
        'true')


if __name__ == '__main__':
  unittest.main()
