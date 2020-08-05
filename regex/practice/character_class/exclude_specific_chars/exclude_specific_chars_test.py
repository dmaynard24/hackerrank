import unittest, exclude_specific_chars


class TestExcludeSpecificChars(unittest.TestCase):
  def test_exclude_specific_chars(self):
    self.assertEqual(exclude_specific_chars.exclude_specific_chars('think?'),
                     'true')


if __name__ == '__main__':
  unittest.main()
