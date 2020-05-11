import unittest, kaprekar_numbers


class TestKaprekarNumbers(unittest.TestCase):
  def test_kaprekar_numbers(self):
    self.assertEqual(kaprekar_numbers.kaprekar_numbers(1, 100),
                     [1, 9, 45, 55, 99])
    self.assertEqual(kaprekar_numbers.kaprekar_numbers(100, 300), [297])
    self.assertEqual(kaprekar_numbers.kaprekar_numbers(400, 700),
                     'INVALID RANGE')


if __name__ == '__main__':
  unittest.main()
