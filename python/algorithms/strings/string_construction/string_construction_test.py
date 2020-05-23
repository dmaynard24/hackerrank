import unittest, string_construction


class TestStringConstruction(unittest.TestCase):
  def test_string_construction(self):
    self.assertEqual(string_construction.string_construction('abcd'), 4)
    self.assertEqual(string_construction.string_construction('abab'), 2)
    self.assertEqual(string_construction.string_construction('scfg'), 4)
    self.assertEqual(string_construction.string_construction('bccb'), 2)


if __name__ == '__main__':
  unittest.main()
