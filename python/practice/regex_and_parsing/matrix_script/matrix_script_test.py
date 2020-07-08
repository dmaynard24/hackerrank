import unittest, matrix_script


class TestMatrixScript(unittest.TestCase):
  def test_matrix_script(self):
    self.assertEqual(
        matrix_script.matrix_script(
            ['Tsi', 'h%x', 'i #', 'sM ', '$a ', '#t%', 'ir!']),
        'This is Matrix#  %!')


if __name__ == '__main__':
  unittest.main()
