import unittest, capitalize


class TestCapitalize(unittest.TestCase):
  def test_capitalize(self):
    self.assertEqual(capitalize.capitalize('hello world'), 'Hello World')


if __name__ == '__main__':
  unittest.main()
