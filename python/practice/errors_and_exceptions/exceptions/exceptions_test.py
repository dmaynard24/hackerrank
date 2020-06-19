import unittest, exceptions


class TestExceptions(unittest.TestCase):
  def test_exceptions(self):
    self.assertEqual(exceptions.exceptions('1', '0'),
                     'Error Code: integer division or modulo by zero')
    self.assertEqual(
        exceptions.exceptions('2', '$'),
        'Error Code: invalid literal for int() with base 10: \'$\'')
    self.assertEqual(exceptions.exceptions('3', '1'), 3)


if __name__ == '__main__':
  unittest.main()
