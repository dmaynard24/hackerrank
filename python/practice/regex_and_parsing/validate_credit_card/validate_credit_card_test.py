import unittest, validate_credit_card


class TestValidateCreditCard(unittest.TestCase):
  def test_validate_credit_card(self):
    self.assertEqual(
        validate_credit_card.validate_credit_card('4123456789123456'), True)

  def test_validate_credit_card_1(self):
    self.assertEqual(
        validate_credit_card.validate_credit_card('5123-4567-8912-3456'), True)

  def test_validate_credit_card_2(self):
    self.assertEqual(
        validate_credit_card.validate_credit_card('61234-567-8912-3456'),
        False)

  def test_validate_credit_card_3(self):
    self.assertEqual(
        validate_credit_card.validate_credit_card('4123356789123456'), True)

  def test_validate_credit_card_4(self):
    self.assertEqual(
        validate_credit_card.validate_credit_card('5133-3367-8912-3456'),
        False)

  def test_validate_credit_card_4(self):
    self.assertEqual(
        validate_credit_card.validate_credit_card('5123 - 3567 - 8912 - 3456'),
        False)


if __name__ == '__main__':
  unittest.main()
