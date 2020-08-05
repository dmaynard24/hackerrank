import unittest, match_word_boundaries


class TestMatchWordBoundaries(unittest.TestCase):
  def test_match_word_boundaries(self):
    self.assertEqual(
        match_word_boundaries.match_word_boundaries('Found any match?'),
        'true')


if __name__ == '__main__':
  unittest.main()
