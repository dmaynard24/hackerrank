import unittest, get_word_counts


class TestGetWordCounts(unittest.TestCase):
  def test_get_word_counts(self):
    self.assertEqual(
        get_word_counts.get_word_counts(
            ['foo bar (foo) bar foo-bar foo_bar foo\'bar bar-foo bar, foo.'],
            ['foo']), '6')


if __name__ == '__main__':
  unittest.main()
