import unittest, alternating_characters


class TestAlternatingCharacters(unittest.TestCase):
  def test_alternating_characters(self):
    self.assertEqual(alternating_characters.alternating_characters('AAAA'), 3)

  def test_alternating_characters_1(self):
    self.assertEqual(alternating_characters.alternating_characters('BBBBB'), 4)

  def test_alternating_characters_2(self):
    self.assertEqual(alternating_characters.alternating_characters('ABABABAB'),
                     0)

  def test_alternating_characters_3(self):
    self.assertEqual(alternating_characters.alternating_characters('BABABA'),
                     0)

  def test_alternating_characters_4(self):
    self.assertEqual(alternating_characters.alternating_characters('AAABBB'),
                     4)


if __name__ == '__main__':
  unittest.main()
