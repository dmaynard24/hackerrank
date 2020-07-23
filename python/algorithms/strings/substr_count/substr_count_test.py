import unittest, substr_count


class TestSubstrCount(unittest.TestCase):
  def test_substr_count(self):
    self.assertEqual(substr_count.substr_count(5, 'asasd'), 7)

  def test_substr_count_1(self):
    self.assertEqual(substr_count.substr_count(7, 'abcbaba'), 10)

  def test_substr_count_2(self):
    self.assertEqual(substr_count.substr_count(4, 'aaaa'), 10)


if __name__ == '__main__':
  unittest.main()
