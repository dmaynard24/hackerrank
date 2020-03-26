import unittest, equalize_array


class TestEqualizeArray(unittest.TestCase):
  def test_equalize_array(self):
    self.assertEqual(equalize_array.equalize_array([37, 32, 97, 35, 76, 62]),
                     5)
    self.assertEqual(equalize_array.equalize_array([3, 3, 2, 1, 3]), 2)


if __name__ == '__main__':
  unittest.main()
