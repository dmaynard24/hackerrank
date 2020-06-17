import unittest, permutations


class TestPermutations(unittest.TestCase):
  def test_permutations(self):
    self.assertEqual(permutations.permutations('HACK', '2'), '''AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH''')


if __name__ == '__main__':
  unittest.main()
