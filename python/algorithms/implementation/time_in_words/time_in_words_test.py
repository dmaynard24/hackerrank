import unittest, time_in_words


class TestTimeInWords(unittest.TestCase):
  def test_time_in_words(self):
    self.assertEqual(time_in_words.time_in_words(5, 47),
                     'thirteen minutes to six')
    self.assertEqual(time_in_words.time_in_words(3, 00), 'three o\' clock')
    self.assertEqual(time_in_words.time_in_words(7, 15), 'quarter past seven')
    self.assertEqual(time_in_words.time_in_words(1, 1), 'one minute past one')
    self.assertEqual(time_in_words.time_in_words(1, 21),
                     'twenty one minutes past one')


if __name__ == '__main__':
  unittest.main()
