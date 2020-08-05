import unittest, match_x_repetitions


class TestMatchXRepetitions(unittest.TestCase):
  def match_x_repetitions(self):
    self.assertEqual(
        match_x_repetitions.match_x_repetitions(
            '2222222222aaaaaaaaaa2222222222aaaaaaaaaa13 57'), 'true')


if __name__ == '__main__':
  unittest.main()
