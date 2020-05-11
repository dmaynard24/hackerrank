import unittest, bigger_is_greater


class TestBiggerIsGreater(unittest.TestCase):
  def test_bigger_is_greater(self):
    self.assertEqual(bigger_is_greater.bigger_is_greater('ab'), 'ba')
    self.assertEqual(bigger_is_greater.bigger_is_greater('bb'), 'no answer')
    self.assertEqual(bigger_is_greater.bigger_is_greater('hefg'), 'hegf')
    self.assertEqual(bigger_is_greater.bigger_is_greater('dhck'), 'dhkc')
    self.assertEqual(bigger_is_greater.bigger_is_greater('dkhc'), 'hcdk')


if __name__ == '__main__':
  unittest.main()
