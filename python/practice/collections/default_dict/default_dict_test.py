import unittest, default_dict


class TestDefaultDict(unittest.TestCase):
  def test_default_dict(self):
    self.assertEqual(
        default_dict.default_dict(['a', 'a', 'b', 'a', 'b'], ['a', 'b']),
        '''1 2 4
3 5''')


if __name__ == '__main__':
  unittest.main()