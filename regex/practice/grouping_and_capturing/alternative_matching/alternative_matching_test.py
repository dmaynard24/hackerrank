import unittest, alternative_matching


class TestAlternativeMatching(unittest.TestCase):
  def alternative_matching(self):
    self.assertEqual(alternative_matching.alternative_matching('Mr.DOSHI'),
                     'true')


if __name__ == '__main__':
  unittest.main()
