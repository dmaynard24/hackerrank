import unittest, input


class TestInput(unittest.TestCase):
  def test_input(self):
    self.assertEqual(input.input(1, 4, 'x**3 + x**2 + x + 1'), True)


if __name__ == '__main__':
  unittest.main()
