import unittest, staircase


class TestStaircase(unittest.TestCase):
  def test_staircase(self):
    self.assertEqual(staircase.staircase(6), '''     #
    ##
   ###
  ####
 #####
######
''')


if __name__ == '__main__':
  unittest.main()
