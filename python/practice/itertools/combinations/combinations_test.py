import unittest, combinations


class TestCombinations(unittest.TestCase):
  def test_combinations(self):
    self.assertEqual(combinations.combinations('HACK', '2'), '''A
C
H
K
AC
AH
AK
CH
CK
HK''')


if __name__ == '__main__':
  unittest.main()
