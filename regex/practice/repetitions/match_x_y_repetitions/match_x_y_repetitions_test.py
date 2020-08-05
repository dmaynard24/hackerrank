import unittest, match_x_y_repetitions


class TestMatchXYRepetitions(unittest.TestCase):
  def test_match_x_y_repetitions(self):
    self.assertEqual(
        match_x_y_repetitions.match_x_y_repetitions('3threeormorealphabets.'),
        'true')


if __name__ == '__main__':
  unittest.main()
