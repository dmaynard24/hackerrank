import unittest, strange_counter


class TestStrangeCounter(unittest.TestCase):
  def test_strange_counter(self):
    self.assertEqual(strange_counter.strange_counter(4), 6)
    self.assertEqual(strange_counter.strange_counter(17), 5)


if __name__ == '__main__':
  unittest.main()
