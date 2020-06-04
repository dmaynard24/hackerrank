import unittest, string_validation


class TestStringValidation(unittest.TestCase):
  def test_string_validation(self):
    self.assertEqual(string_validation.string_validation('qA2'),
                     [True, True, True, True, True])


if __name__ == '__main__':
  unittest.main()
