import unittest, day_of_the_programmer


class TestDayOfTheProgrammer(unittest.TestCase):
  def test_day_of_the_programmer(self):
    self.assertEqual(day_of_the_programmer.day_of_the_programmer(2017),
                     '13.09.2017')
    self.assertEqual(day_of_the_programmer.day_of_the_programmer(2016),
                     '12.09.2016')
    self.assertEqual(day_of_the_programmer.day_of_the_programmer(1918),
                     '26.09.1918')
    self.assertEqual(day_of_the_programmer.day_of_the_programmer(1800),
                     '12.09.1800')


if __name__ == '__main__':
  unittest.main()
