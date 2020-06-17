import unittest, iterables_and_iterators


class TestIterablesAndIterators(unittest.TestCase):
  def test_iterables_and_iterators(self):
    self.assertEqual(
        iterables_and_iterators.iterables_and_iterators(
            4, ['a', 'a', 'c', 'd'], 2), 0.8333333333333334)


if __name__ == '__main__':
  unittest.main()
