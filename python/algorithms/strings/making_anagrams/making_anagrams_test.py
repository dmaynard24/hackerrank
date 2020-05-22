import unittest, making_anagrams


class TestMakingAnagrams(unittest.TestCase):
  def test_making_anagrams(self):
    self.assertEqual(making_anagrams.making_anagrams('cde', 'abc'), 4)
    self.assertEqual(
        making_anagrams.making_anagrams(
            'absdjkvuahdakejfnfauhdsaavasdlkj',
            'djfladfhiawasdkjvalskufhafablsdkashlahdfa'), 19)


if __name__ == '__main__':
  unittest.main()
