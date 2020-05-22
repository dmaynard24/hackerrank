import unittest, anagram


class TestAnagram(unittest.TestCase):
  def test_anagram(self):
    self.assertEqual(anagram.anagram('aaabbb'), 3)
    self.assertEqual(anagram.anagram('ab'), 1)
    self.assertEqual(anagram.anagram('abc'), -1)
    self.assertEqual(anagram.anagram('mnop'), 2)
    self.assertEqual(anagram.anagram('xyyx'), 0)
    self.assertEqual(anagram.anagram('xaxbbbxx'), 1)
    self.assertEqual(anagram.anagram('asdfjoieufoa'), 3)
    self.assertEqual(anagram.anagram('fdhlvosfpafhalll'), 5)
    self.assertEqual(anagram.anagram('mvdalvkiopaufl'), 5)


if __name__ == '__main__':
  unittest.main()
