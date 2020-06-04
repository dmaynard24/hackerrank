import unittest, print_formatted


class TestPrintFormatted(unittest.TestCase):
  def test_print_formatted(self):
    self.assertEqual(print_formatted.print_formatted(2),
                     [' 1  1  1  1', ' 2  2  2 10'])


if __name__ == '__main__':
  unittest.main()
