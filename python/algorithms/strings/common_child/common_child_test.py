import unittest, common_child


class TestCommonChild(unittest.TestCase):
  def test_common_child(self):
    self.assertEqual(common_child.common_child('HARRY', 'SALLY'), 2)

  def test_common_child_1(self):
    self.assertEqual(common_child.common_child('AA', 'BB'), 0)

  def test_common_child_2(self):
    self.assertEqual(common_child.common_child('SHINCHAN', 'NOHARAAA'), 3)

  def test_common_child_3(self):
    self.assertEqual(common_child.common_child('ABCDEF', 'FBDAMN'), 2)

  def test_common_child_4(self):
    self.assertEqual(
        common_child.common_child(
            'WEWOUCUIDGCGTRMEZEPXZFEJWISRSBBSYXAYDFEJJDLEBVHHKS',
            'FDAGCXGKCTKWNECHMRXZWMLRYUCOCZHJRRJBOAJOQJZZVUYXIC'), 15)


if __name__ == '__main__':
  unittest.main()
