import unittest, swap_case


class TestSwapCase(unittest.TestCase):
  def test_swap_case(self):
    self.assertEqual(
        swap_case.swap_case('HackerRank.com presents "Pythonist 2".'),
        'hACKERrANK.COM PRESENTS "pYTHONIST 2".')


if __name__ == '__main__':
  unittest.main()
