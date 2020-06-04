import unittest, count_substrings


class TestCountSubstrings(unittest.TestCase):
  def test_count_substrings(self):
    self.assertEqual(count_substrings.count_substrings('ABCDCDC', 'CDC'), 2)


if __name__ == '__main__':
  unittest.main()
