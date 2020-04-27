import unittest, kangaroo


class TestKangaroo(unittest.TestCase):
  def test_kangaroo(self):
    self.assertEqual(kangaroo.kangaroo(0, 3, 4, 2), 'YES')
    self.assertEqual(kangaroo.kangaroo(0, 2, 5, 3), 'NO')


if __name__ == '__main__':
  unittest.main()
