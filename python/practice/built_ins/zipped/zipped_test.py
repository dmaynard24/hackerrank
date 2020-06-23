import unittest, zipped


class TestZipped(unittest.TestCase):
  def test_zipped(self):
    self.assertEqual(
        zipped.zipped([[89, 90, 78, 93, 80], [90, 91, 85, 88, 86],
                       [91, 92, 83, 89, 90.5]], 3),
        [90.0, 91.0, 82.0, 90.0, 85.5])


if __name__ == '__main__':
  unittest.main()
