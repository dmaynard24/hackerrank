import unittest, merge_the_tools


class TestMergeTheTools(unittest.TestCase):
  def test_merge_the_tools(self):
    self.assertEqual(merge_the_tools.merge_the_tools('AABCAAADA', 3), '''AB
CA
AD''')


if __name__ == '__main__':
  unittest.main()
