import unittest, any_or_all


class TestAnyOrAll(unittest.TestCase):
  def test_any_or_all(self):
    self.assertEqual(any_or_all.any_or_all(['12', '9', '61', '5', '14']), True)


if __name__ == '__main__':
  unittest.main()
