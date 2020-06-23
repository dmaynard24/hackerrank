import unittest, ginorts


class TestGinorts(unittest.TestCase):
  def test_ginorts(self):
    self.assertEqual(ginorts.ginorts('Sorting1234'), 'ginortS1324')


if __name__ == '__main__':
  unittest.main()
