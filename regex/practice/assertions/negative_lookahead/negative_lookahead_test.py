import unittest, negative_lookahead


class TestNegativeLookahead(unittest.TestCase):
  def test_negative_lookahead(self):
    self.assertEqual(negative_lookahead.negative_lookahead('gooooo'),
                     'Number of matches : 2')


if __name__ == '__main__':
  unittest.main()
