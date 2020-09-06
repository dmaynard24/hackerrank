import unittest, get_substring_counts


class TestGetSubstringCounts(unittest.TestCase):
  def test_get_substring_counts(self):
    self.assertEqual(
        get_substring_counts.get_substring_counts(
            ['existing pessimist optimist this is'], ['is']), '3')


if __name__ == '__main__':
  unittest.main()
