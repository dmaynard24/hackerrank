import unittest, validate_phone_number


class TestValidatePhoneNumber(unittest.TestCase):
  def test_validate_phone_number(self):
    self.assertEqual(validate_phone_number.validate_phone_number('8956324712'),
                     'YES')
    self.assertEqual(validate_phone_number.validate_phone_number('FACBGEGADB'),
                     'NO')
    self.assertEqual(
        validate_phone_number.validate_phone_number('85234789651'), 'NO')


if __name__ == '__main__':
  unittest.main()
