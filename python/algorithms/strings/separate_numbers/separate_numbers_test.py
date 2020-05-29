import unittest, separate_numbers


class TestSeparateNumbers(unittest.TestCase):
  def test_separate_numbers(self):
    self.assertEqual(separate_numbers.separate_numbers('1234'), 'YES 1')
    self.assertEqual(separate_numbers.separate_numbers('91011'), 'YES 9')
    self.assertEqual(separate_numbers.separate_numbers('99100'), 'YES 99')
    self.assertEqual(separate_numbers.separate_numbers('101103'), 'NO')
    self.assertEqual(separate_numbers.separate_numbers('010203'), 'NO')
    self.assertEqual(separate_numbers.separate_numbers('10203'), 'NO')
    self.assertEqual(separate_numbers.separate_numbers('13'), 'NO')
    self.assertEqual(separate_numbers.separate_numbers('1'), 'NO')


if __name__ == '__main__':
  unittest.main()
