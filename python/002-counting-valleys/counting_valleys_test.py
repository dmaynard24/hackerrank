import unittest, counting_valleys


class TestCountingValleys(unittest.TestCase):
  def test_counting_valleys(self):
    self.assertEqual(counting_valleys.counting_valleys(8, 'UDDDUDUU'), 1)


if __name__ == '__main__':
  unittest.main()
