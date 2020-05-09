import unittest, taum_bday


class TestTaumBday(unittest.TestCase):
  def test_taum_bday(self):
    self.assertEqual(taum_bday.taum_bday(10, 10, 1, 1, 1), 20)
    self.assertEqual(taum_bday.taum_bday(5, 9, 2, 3, 4), 37)
    self.assertEqual(taum_bday.taum_bday(3, 6, 9, 1, 1), 12)
    self.assertEqual(taum_bday.taum_bday(7, 7, 4, 2, 1), 35)
    self.assertEqual(taum_bday.taum_bday(3, 3, 1, 9, 2), 12)


if __name__ == '__main__':
  unittest.main()
