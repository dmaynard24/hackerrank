import unittest, simple_array_sum


class TestSimpleArraySum(unittest.TestCase):
  def test_simple_array_sum(self):
    self.assertEqual(simple_array_sum.simple_array_sum([1, 2, 3, 4, 10, 11]),
                     31)


if __name__ == '__main__':
  unittest.main()
