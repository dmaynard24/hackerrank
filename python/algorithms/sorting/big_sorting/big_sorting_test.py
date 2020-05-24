import unittest, big_sorting


class TestBigSorting(unittest.TestCase):
  def test_big_sorting(self):
    self.assertEqual(
        big_sorting.big_sorting([
            '1', '2', '100', '12303479849857341718340192371',
            '3084193741082937', '3084193741082938', '111', '200'
        ]), [
            '1', '2', '100', '111', '200', '3084193741082937',
            '3084193741082938', '12303479849857341718340192371'
        ])
    self.assertEqual(
        big_sorting.big_sorting([
            '1', '2', '100', '12303479849857341718340192371',
            '3084193741082937', '3084193741082938', '111', '200'
        ]), [
            '1', '2', '100', '111', '200', '3084193741082937',
            '3084193741082938', '12303479849857341718340192371'
        ])


if __name__ == '__main__':
  unittest.main()
