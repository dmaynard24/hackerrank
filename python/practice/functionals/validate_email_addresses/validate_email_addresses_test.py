import unittest, validate_email_addresses


class TestValidateEmailAddresses(unittest.TestCase):
  def test_validate_email_addresses(self):
    self.assertEqual(
        validate_email_addresses.validate_email_addresses([
            'dheeraj-234@gmail.com', 'itsallcrap', 'harsh_1234@rediff.in',
            'kunal_shin@iop.az', 'matt23@@india.in'
        ]),
        ['dheeraj-234@gmail.com', 'harsh_1234@rediff.in', 'kunal_shin@iop.az'])
    self.assertEqual(
        validate_email_addresses.validate_email_addresses(
            ['harsh@gmail', 'iota_98@hackerrank.com']),
        ['iota_98@hackerrank.com'])


if __name__ == '__main__':
  unittest.main()
