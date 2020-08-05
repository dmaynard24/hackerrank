import unittest, alternative_matching


class TestAlternativeMatching(unittest.TestCase):
  def test_alternative_matching(self):
    self.assertEqual(alternative_matching.alternative_matching('Mr.DOSHI'),
                     'true')

  def test_alternative_matching_1(self):
    self.assertEqual(alternative_matching.alternative_matching('Mrs.DOSHI'),
                     'true')

  def test_alternative_matching_2(self):
    self.assertEqual(alternative_matching.alternative_matching('Miss DOSHI'),
                     'false')

  def test_alternative_matching_3(self):
    self.assertEqual(alternative_matching.alternative_matching('Dr. DOSHI'),
                     'false')


if __name__ == '__main__':
  unittest.main()
