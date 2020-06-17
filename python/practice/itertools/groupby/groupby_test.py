import unittest, groupby


class TestGroupby(unittest.TestCase):
  def test_groupby(self):
    self.assertEqual(groupby.groupby('1222311'), '(1, 1) (3, 2) (1, 3) (2, 1)')


if __name__ == '__main__':
  unittest.main()
