import unittest, love_letter_mystery


class TestLoveLetterMystery(unittest.TestCase):
  def test_love_letter_mystery(self):
    self.assertEqual(love_letter_mystery.love_letter_mystery('abc'), 2)
    self.assertEqual(love_letter_mystery.love_letter_mystery('abcba'), 0)
    self.assertEqual(love_letter_mystery.love_letter_mystery('abcd'), 4)
    self.assertEqual(love_letter_mystery.love_letter_mystery('cba'), 2)
    self.assertEqual(love_letter_mystery.love_letter_mystery('lmnop'), 6)
    self.assertEqual(love_letter_mystery.love_letter_mystery('adslkfjas'), 36)
    self.assertEqual(love_letter_mystery.love_letter_mystery('bafhaef'), 13)
    self.assertEqual(love_letter_mystery.love_letter_mystery('ofrhase'), 40)


if __name__ == '__main__':
  unittest.main()
