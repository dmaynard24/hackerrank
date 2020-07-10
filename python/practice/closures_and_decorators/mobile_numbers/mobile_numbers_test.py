import unittest, mobile_numbers


class TestFindMaxDepth(unittest.TestCase):
  def test_mobile_numbers(self):
    self.assertEqual(
        mobile_numbers.mobile_numbers(
            ['07895462130', '919875641230', '9195969878']), '''+91 78954 62130
+91 91959 69878
+91 98756 41230''')


if __name__ == '__main__':
  unittest.main()