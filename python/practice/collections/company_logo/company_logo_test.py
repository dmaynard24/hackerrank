import unittest, company_logo


class TestDeque(unittest.TestCase):
  def test_company_logo(self):
    self.assertEqual(company_logo.company_logo('aabbbccde'), '''b 3
a 2
c 2''')


if __name__ == '__main__':
  unittest.main()