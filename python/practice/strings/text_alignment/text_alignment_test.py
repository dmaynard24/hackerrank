import unittest, text_alignment


class TestTextAlignment(unittest.TestCase):
  def test_text_alignment(self):
    self.assertEqual(text_alignment.text_alignment(5), [
        '    H    ', 
        '   HHH   ', 
        '  HHHHH  ', 
        ' HHHHHHH ', 
        'HHHHHHHHH',
        '  HHHHH               HHHHH             ',
        '  HHHHH               HHHHH             ',
        '  HHHHH               HHHHH             ',
        '  HHHHH               HHHHH             ',
        '  HHHHH               HHHHH             ',
        '  HHHHH               HHHHH             ',
        '  HHHHHHHHHHHHHHHHHHHHHHHHH   ', 
        '  HHHHHHHHHHHHHHHHHHHHHHHHH   ',
        '  HHHHHHHHHHHHHHHHHHHHHHHHH   ',
        '  HHHHH               HHHHH             ',
        '  HHHHH               HHHHH             ',
        '  HHHHH               HHHHH             ',
        '  HHHHH               HHHHH             ',
        '  HHHHH               HHHHH             ',
        '  HHHHH               HHHHH             ',
        '                    HHHHHHHHH ',
        '                     HHHHHHH  ',
        '                      HHHHH   ',
        '                       HHH    ',
        '                        H     '
    ])


if __name__ == '__main__':
  unittest.main()
