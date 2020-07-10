import unittest, name_directory


class TestNameDirectory(unittest.TestCase):
  def test_name_directory(self):
    self.assertEqual(
        name_directory.name_directory([['Mike', 'Thomson', '20', 'M'],
                                       ['Robert', 'Bustle', '32', 'M'],
                                       ['Andria', 'Bustle', '30', 'F']]),
        '''Mr. Mike Thomson
Ms. Andria Bustle
Mr. Robert Bustle''')


if __name__ == '__main__':
  unittest.main()