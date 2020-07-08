import unittest, validate_postal_code


class TestPostalCode(unittest.TestCase):
  def test_validate_postal_code(self):
    self.assertEqual(validate_postal_code.validate_postal_code('110000'),
                     False)

  def test_validate_postal_code_1(self):
    self.assertEqual(validate_postal_code.validate_postal_code('123456'), True)


if __name__ == '__main__':
  unittest.main()
