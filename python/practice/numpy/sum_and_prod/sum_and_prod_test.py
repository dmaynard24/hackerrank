import unittest, sum_and_prod


class TestEyeAndIdentity(unittest.TestCase):
  def test_sum_and_prod(self):
    self.assertEqual(sum_and_prod.sum_and_prod([[1, 2], [3, 4]]), 24)


if __name__ == '__main__':
  unittest.main()