import unittest, words_score


class TestWordsScore(unittest.TestCase):
  def test_words_score(self):
    self.assertEqual(words_score.score_words('hacker book'.split()), 4)

  def test_words_score_1(self):
    self.assertEqual(words_score.score_words('programming is awesome'.split()),
                     4)


if __name__ == '__main__':
  unittest.main()