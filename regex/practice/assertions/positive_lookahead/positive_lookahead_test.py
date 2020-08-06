import unittest, positive_lookahead


class TestPositiveLookahead(unittest.TestCase):
  def test_positive_lookahead(self):
    self.assertEqual(positive_lookahead.positive_lookahead('gooooo!'),
                     'Number of matches : 3')


if __name__ == '__main__':
  unittest.main()
