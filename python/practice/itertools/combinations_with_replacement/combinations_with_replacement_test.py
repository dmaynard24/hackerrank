import unittest, combinations_with_replacement


class TestCombinationsWithReplacement(unittest.TestCase):
  def test_combinations_with_replacement(self):
    self.assertEqual(
        combinations_with_replacement.combinations_with_replacement(
            'HACK', '2'), '''AA
AC
AH
AK
CC
CH
CK
HH
HK
KK''')


if __name__ == '__main__':
  unittest.main()
