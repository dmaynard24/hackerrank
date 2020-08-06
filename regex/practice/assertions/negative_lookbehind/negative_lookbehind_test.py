import unittest, negative_lookbehind


class TestNegativeLookbehind(unittest.TestCase):
  def test_negative_lookbehind(self):
    self.assertEqual(negative_lookbehind.negative_lookbehind('1o1s'),
                     'Number of matches : 3')


if __name__ == '__main__':
  unittest.main()
