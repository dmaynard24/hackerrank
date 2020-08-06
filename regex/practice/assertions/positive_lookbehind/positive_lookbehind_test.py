import unittest, positive_lookbehind


class TestPositiveLookbehind(unittest.TestCase):
  def test_positive_lookbehind(self):
    self.assertEqual(positive_lookbehind.positive_lookbehind('123Go!'),
                     'Number of matches : 1')


if __name__ == '__main__':
  unittest.main()
