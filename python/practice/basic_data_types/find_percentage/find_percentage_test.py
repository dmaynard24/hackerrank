import unittest, find_percentage


class TestFindPercentage(unittest.TestCase):
  def test_find_percentage(self):
    self.assertEqual(
        find_percentage.find_percentage(
            {
                'Krishna': [67, 68, 69],
                'Arjun': [70, 98, 63],
                'Malika': [52, 56, 60]
            }, 'Malika'), '56.00')
    self.assertEqual(
        find_percentage.find_percentage(
            {
                'Harsh': [25, 26.5, 28],
                'Anurag': [26, 28, 30],
            }, 'Harsh'), '26.50')


if __name__ == '__main__':
  unittest.main()
