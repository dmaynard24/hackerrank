import unittest, arrays


class TestArrays(unittest.TestCase):
  def test_arrays(self):
    self.assertEqual(arrays.arrays([1, 2, 3, 4, -8, -10]),
                     '[-10.  -8.   4.   3.   2.   1.]')


if __name__ == '__main__':
  unittest.main()