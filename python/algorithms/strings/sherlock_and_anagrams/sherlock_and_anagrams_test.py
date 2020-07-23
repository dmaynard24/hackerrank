import unittest, sherlock_and_anagrams


class TestSherlockAndAnagrams(unittest.TestCase):
  def test_sherlock_and_anagrams(self):
    self.assertEqual(sherlock_and_anagrams.sherlock_and_anagrams('abba'), 4)

  def test_sherlock_and_anagrams_1(self):
    self.assertEqual(sherlock_and_anagrams.sherlock_and_anagrams('abcd'), 0)

  def test_sherlock_and_anagrams_2(self):
    self.assertEqual(sherlock_and_anagrams.sherlock_and_anagrams('ifailuhkqq'),
                     3)

  def test_sherlock_and_anagrams_3(self):
    self.assertEqual(sherlock_and_anagrams.sherlock_and_anagrams('kkkk'), 10)


if __name__ == '__main__':
  unittest.main()
