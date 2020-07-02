import unittest, validate_named_email


class TestValidateNamedEmail(unittest.TestCase):
  def test_validate_named_email(self):
    self.assertEqual(
        validate_named_email.validate_named_email(
            'DEXTER <dexter@hotmail.com>'), True)
    self.assertEqual(
        validate_named_email.validate_named_email(
            'VIRUS <virus!@variable.:p>'), False)
    self.assertEqual(
        validate_named_email.validate_named_email(
            'dheeraj <dheeraj-234@gmail.com>'), True)
    self.assertEqual(
        validate_named_email.validate_named_email('crap <itsallcrap>'), False)
    self.assertEqual(
        validate_named_email.validate_named_email(
            'harsh <harsh_1234@rediff.in>'), True)
    self.assertEqual(
        validate_named_email.validate_named_email('kumal <kunal_shin@iop.az>'),
        True)
    self.assertEqual(
        validate_named_email.validate_named_email('mattp <matt23@@india.in>'),
        False)
    self.assertEqual(
        validate_named_email.validate_named_email(
            'harsh <.harsh_1234@rediff.in>'), False)
    self.assertEqual(
        validate_named_email.validate_named_email(
            'harsh <-harsh_1234@rediff.in>'), False)


if __name__ == '__main__':
  unittest.main()
