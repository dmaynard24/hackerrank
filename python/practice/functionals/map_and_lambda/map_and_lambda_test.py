import unittest, map_and_lambda


class TestMapAndLambda(unittest.TestCase):
  def test_map_and_lambda(self):
    self.assertEqual(list(map(lambda x: x**3, map_and_lambda.fibonacci(5))),
                     [0, 1, 1, 8, 27])


if __name__ == '__main__':
  unittest.main()
