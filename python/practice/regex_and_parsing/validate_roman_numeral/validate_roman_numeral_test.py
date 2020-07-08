import unittest, validate_roman_numeral


class TestValidateRomanNumeral(unittest.TestCase):
  def test_validate_roman_numeral(self):
    self.assertEqual(validate_roman_numeral.validate_roman_numeral('CDXXI'),
                     True)

  def test_validate_roman_numeral_1(self):
    self.assertEqual(validate_roman_numeral.validate_roman_numeral('DXXVIIII'),
                     False)

  def test_validate_roman_numeral_2(self):
    self.assertEqual(validate_roman_numeral.validate_roman_numeral('LL'),
                     False)

  def test_validate_roman_numeral_3(self):
    self.assertEqual(
        validate_roman_numeral.validate_roman_numeral('MMMCMXCIX'), True)


if __name__ == '__main__':
  unittest.main()