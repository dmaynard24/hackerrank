import unittest, super_reduced_string


class TestSuperReducedString(unittest.TestCase):
  def test_super_reduced_string(self):
    self.assertEqual(super_reduced_string.super_reduced_string('aaabccddd'),
                     'abd')
    self.assertEqual(super_reduced_string.super_reduced_string('baab'),
                     'Empty String')
    self.assertEqual(super_reduced_string.super_reduced_string('aa'),
                     'Empty String')


if __name__ == '__main__':
  unittest.main()
