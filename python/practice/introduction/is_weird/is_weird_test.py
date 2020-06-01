import unittest, is_weird


class TestIsWeird(unittest.TestCase):
  def test_is_weird(self):
    self.assertEqual(is_weird.is_weird(3), 'Weird')
    self.assertEqual(is_weird.is_weird(24), 'Not Weird')


if __name__ == '__main__':
  unittest.main()
