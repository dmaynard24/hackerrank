import unittest, cat_and_mouse


class TestCatAndMouse(unittest.TestCase):
  def test_cat_and_mouse(self):
    self.assertEqual(cat_and_mouse.cat_and_mouse(1, 2, 3), 'Cat B')
    self.assertEqual(cat_and_mouse.cat_and_mouse(1, 3, 2), 'Mouse C')


if __name__ == '__main__':
  unittest.main()
