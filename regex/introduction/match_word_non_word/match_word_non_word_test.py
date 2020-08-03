import unittest, match_word_non_word


class TestMatchWordNonWord(unittest.TestCase):
  def test_match_word_non_word(self):
    self.assertEqual(
        match_word_non_word.match_word_non_word('www.hackerrank.com'), 'true')


if __name__ == '__main__':
  unittest.main()
