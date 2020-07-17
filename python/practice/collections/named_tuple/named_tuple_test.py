import unittest, named_tuple


class TestNamedTuple(unittest.TestCase):
  def test_named_tuple(self):
    self.assertEqual(
        named_tuple.named_tuple('ID         MARKS      NAME       CLASS    ', [
            '1          97         Raymond    7         ',
            '2          50         Steven     4         ',
            '3          91         Adrian     9         ',
            '4          72         Stewart    5         ',
            '5          80         Peter      6'
        ]), 78)

  def test_named_tuple_1(self):
    self.assertEqual(
        named_tuple.named_tuple('MARKS      CLASS      NAME       ID       ', [
            '92         2          Calum      1         ',
            '82         5          Scott      2         ',
            '94         2          Jason      3         ',
            '55         8          Glenn      4         ',
            '82         2          Fergus     5'
        ]), 81)


if __name__ == '__main__':
  unittest.main()