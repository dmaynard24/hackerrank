import unittest, hex_color_code


class TestHexColorCode(unittest.TestCase):
  def test_hex_color_code(self):
    self.assertEqual(
        hex_color_code.hex_color_code('''#BED
{
    color: #FfFdF8; background-color:#aef;
    font-size: 123px;
    background: -webkit-linear-gradient(top, #f9f9f9, #fff);
}
#Cab
{
    background-color: #ABC;
    border: 2px dashed #fff;
}   '''), '''#FfFdF8
#aef
#f9f9f9
#fff
#ABC
#fff''')


if __name__ == '__main__':
  unittest.main()
