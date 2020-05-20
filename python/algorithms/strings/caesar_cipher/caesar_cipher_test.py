import unittest, caesar_cipher


class TestCaesarCipher(unittest.TestCase):
  def test_caesar_cipher(self):
    self.assertEqual(caesar_cipher.caesar_cipher('middle-Outz', 2),
                     'okffng-Qwvb')
    self.assertEqual(caesar_cipher.caesar_cipher('Hello_World!', 4),
                     'Lipps_Asvph!')
    self.assertEqual(
        caesar_cipher.caesar_cipher('Always-Look-on-the-Bright-Side-of-Life',
                                    5),
        'Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj')


if __name__ == '__main__':
  unittest.main()
