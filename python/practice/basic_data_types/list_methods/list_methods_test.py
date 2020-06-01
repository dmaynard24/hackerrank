import unittest, list_methods


class TestListMethods(unittest.TestCase):
  def test_list_methods(self):
    self.assertEqual(
        list_methods.list_methods([['insert', '0', '5'], ['insert', '1', '10'],
                                   ['insert', '0', '6'], ['print'],
                                   ['remove', '6'], ['append', '9'],
                                   ['append', '1'], ['sort'], ['print'],
                                   ['pop'], ['reverse'], ['print']]),
        [[6, 5, 10], [1, 5, 9, 10], [9, 5, 1]])


if __name__ == '__main__':
  unittest.main()
