import unittest, mutate_string


class TestMutateString(unittest.TestCase):
  def test_mutate_string(self):
    self.assertEqual(mutate_string.mutate_string('abracadabra', 5, 'k'),
                     'abrackdabra')


if __name__ == '__main__':
  unittest.main()
