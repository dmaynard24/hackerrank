import unittest, full_counting_sort


class TestFullCountingSort(unittest.TestCase):
  def test_full_counting_sort(self):
    self.assertEqual(
        full_counting_sort.full_counting_sort([
            ['0', 'ab'],
            ['6', 'cd'],
            ['0', 'ef'],
            ['6', 'gh'],
            ['4', 'ij'],
            ['0', 'ab'],
            ['6', 'cd'],
            ['0', 'ef'],
            ['6', 'gh'],
            ['0', 'ij'],
            ['4', 'that'],
            ['3', 'be'],
            ['0', 'to'],
            ['1', 'be'],
            ['5', 'question'],
            ['1', 'or'],
            ['2', 'not'],
            ['4', 'is'],
            ['2', 'to'],
            ['4', 'the'],
        ]), '- - - - - to be or not to be - that is the question - - - -')


if __name__ == '__main__':
  unittest.main()
