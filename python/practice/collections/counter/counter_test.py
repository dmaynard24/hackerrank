import unittest, counter


class TestCounter(unittest.TestCase):
  def test_counter(self):
    self.assertEqual(
        counter.counter(
            [2, 3, 4, 5, 6, 8, 7, 6, 5, 18],
            [[6, 55], [6, 45], [6, 55], [4, 40], [18, 60], [10, 50]]), 200)


if __name__ == '__main__':
  unittest.main()