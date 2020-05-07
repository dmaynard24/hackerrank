import unittest, append_and_delete


class TestAppendAndDelete(unittest.TestCase):
  def test_append_and_delete(self):
    self.assertEqual(
        append_and_delete.append_and_delete('hackerhappy', 'hackerrank', 9),
        'Yes')
    self.assertEqual(append_and_delete.append_and_delete('aba', 'aba', 7),
                     'Yes')
    self.assertEqual(append_and_delete.append_and_delete('ashley', 'ash', 2),
                     'No')
    self.assertEqual(append_and_delete.append_and_delete('y', 'yu', 2), 'No')


if __name__ == '__main__':
  unittest.main()
