import unittest, match_start_end


class TestMatchStartEnd(unittest.TestCase):
  def test_match_start_end(self):
    self.assertEqual(match_start_end.match_start_end('0qwer.'), 'true')


if __name__ == '__main__':
  unittest.main()
