import unittest, gemstones


class TestGemstones(unittest.TestCase):
  def test_gemstones(self):
    self.assertEqual(gemstones.gemstones(['abcdde', 'baccd', 'eeabg']), 2)
    self.assertEqual(
        gemstones.gemstones(
            ['basdfj', 'asdlkjfdjsa', 'bnafvfnsd', 'oafhdlasd']), 4)
    self.assertEqual(
        gemstones.gemstones(['vtrjvgbj', 'mkmjyaeav', 'sibzdmsk']), 0)


if __name__ == '__main__':
  unittest.main()
