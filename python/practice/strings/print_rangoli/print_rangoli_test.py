import unittest, print_rangoli


class TestPrintRangoli(unittest.TestCase):
  def test_print_rangoli(self):
    self.assertEqual(
        print_rangoli.print_rangoli(5), '''--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------''')


if __name__ == '__main__':
  unittest.main()
