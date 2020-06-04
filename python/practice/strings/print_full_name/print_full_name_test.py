import unittest, print_full_name


class TestPrintFullName(unittest.TestCase):
  def test_print_full_name(self):
    self.assertEqual(print_full_name.print_full_name('Dave', 'Maynard'),
                     'Hello Dave Maynard! You just delved into python.')


if __name__ == '__main__':
  unittest.main()
