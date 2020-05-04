import unittest, save_the_prisoner


class TestSaveThePrisoner(unittest.TestCase):
  def test_save_the_prisoner(self):
    self.assertEqual(save_the_prisoner.save_the_prisoner(5, 2, 1), 2)
    self.assertEqual(save_the_prisoner.save_the_prisoner(5, 2, 2), 3)
    self.assertEqual(save_the_prisoner.save_the_prisoner(7, 19, 2), 6)
    self.assertEqual(save_the_prisoner.save_the_prisoner(3, 7, 3), 3)


if __name__ == '__main__':
  unittest.main()
