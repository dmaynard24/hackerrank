import unittest, print_integer


class TestPrintInteger(unittest.TestCase):
  def test_print_integer(self):
    self.assertEqual(print_integer.print_integer(3), 123)
    self.assertEqual(print_integer.print_integer(13), 12345678910111213)


if __name__ == '__main__':
  unittest.main()
