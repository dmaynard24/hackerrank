import unittest, pangram


class TestPangram(unittest.TestCase):
  def test_pangram(self):
    self.assertEqual(
        pangram.pangram(
            'We promptly judged antique ivory buckles for the next prize'),
        'pangram')
    self.assertEqual(
        pangram.pangram(
            'We promptly judged antique ivory buckles for the prize'),
        'not pangram')


if __name__ == '__main__':
  unittest.main()
