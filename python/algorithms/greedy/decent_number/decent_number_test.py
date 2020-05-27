import unittest, decent_number


class TestDecentNumber(unittest.TestCase):
  def test_decent_number(self):
    self.assertEqual(decent_number.decent_number(1), '-1')
    self.assertEqual(decent_number.decent_number(3), '555')
    self.assertEqual(decent_number.decent_number(5), '33333')
    self.assertEqual(decent_number.decent_number(11), '55555533333')


if __name__ == '__main__':
  unittest.main()
