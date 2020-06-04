import unittest, split_and_join


class TestSwapCase(unittest.TestCase):
  def test_split_and_join(self):
    self.assertEqual(split_and_join.split_and_join('this is a string'),
                     'this-is-a-string')


if __name__ == '__main__':
  unittest.main()
