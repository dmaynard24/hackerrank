import unittest, eval


class TestEval(unittest.TestCase):
  def test_eval(self):
    self.assertEqual(eval.practice_eval('1 + 4'), 5)


if __name__ == '__main__':
  unittest.main()
