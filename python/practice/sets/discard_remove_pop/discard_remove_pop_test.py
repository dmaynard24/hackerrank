import unittest, discard_remove_pop


class TestDiscardRemovePop(unittest.TestCase):
  def test_discard_remove_pop(self):
    self.assertEqual(
        discard_remove_pop.discard_remove_pop([1, 2, 3, 4, 5, 6, 7, 8, 9], [
            'pop', 'remove 9', 'discard 9', 'discard 8', 'remove 7', 'pop',
            'discard 6', 'remove 5', 'pop', 'discard 5'
        ]), 4)


if __name__ == '__main__':
  unittest.main()
