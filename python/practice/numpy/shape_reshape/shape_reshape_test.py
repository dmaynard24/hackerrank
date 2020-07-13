import unittest, shape_reshape


class TestShapeReshape(unittest.TestCase):
  def test_shape_reshape(self):
    self.assertEqual(shape_reshape.shape_reshape([1, 2, 3, 4, 5, 6, 7, 8, 9]),
                     '''[[1 2 3]
 [4 5 6]
 [7 8 9]]''')


if __name__ == '__main__':
  unittest.main()