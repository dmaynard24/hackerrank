import unittest, detect_float


class TestDetectFloat(unittest.TestCase):
  def test_detect_float(self):
    self.assertEqual(detect_float.detect_float('4.0O0'), False)
    self.assertEqual(detect_float.detect_float('-1.00'), True)
    self.assertEqual(detect_float.detect_float('+4.54'), True)
    self.assertEqual(detect_float.detect_float('SomeRandomStuff'), False)


if __name__ == '__main__':
  unittest.main()
