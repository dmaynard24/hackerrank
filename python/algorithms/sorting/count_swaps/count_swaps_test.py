from io import StringIO
from unittest.mock import patch
import unittest, count_swaps


class TestCountSwaps(unittest.TestCase):
  def test_count_swaps(self):
    with patch('sys.stdout', new=StringIO()) as fake_out:
      count_swaps.count_swaps([6, 4, 1])
      self.assertEqual(
          fake_out.getvalue(), '''Array is sorted in 3 swaps.
First Element: 1
Last Element: 6
''')

  def test_count_swaps_1(self):
    with patch('sys.stdout', new=StringIO()) as fake_out:
      count_swaps.count_swaps([1, 2, 3])
      self.assertEqual(
          fake_out.getvalue(), '''Array is sorted in 0 swaps.
First Element: 1
Last Element: 3
''')

  def test_count_swaps_2(self):
    with patch('sys.stdout', new=StringIO()) as fake_out:
      count_swaps.count_swaps([3, 2, 1])
      self.assertEqual(
          fake_out.getvalue(), '''Array is sorted in 3 swaps.
First Element: 1
Last Element: 3
''')


if __name__ == '__main__':
  unittest.main()
