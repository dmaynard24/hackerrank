import unittest, utopian_tree


class TestUtopianTree(unittest.TestCase):
  def test_utopian_tree(self):
    self.assertEqual(utopian_tree.utopian_tree(0), 1)
    self.assertEqual(utopian_tree.utopian_tree(1), 2)
    self.assertEqual(utopian_tree.utopian_tree(4), 7)


if __name__ == '__main__':
  unittest.main()
