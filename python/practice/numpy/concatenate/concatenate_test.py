import unittest, concatenate


class TestConcatenate(unittest.TestCase):
  def test_concatenate(self):
    self.assertEqual(
        concatenate.concatenate([[1, 2], [1, 2], [1, 2], [1, 2], [3, 4],
                                 [3, 4], [3, 4]]), '''[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]]''')


if __name__ == '__main__':
  unittest.main()