import unittest, encryption


class TestEncryption(unittest.TestCase):
  def test_encryption(self):
    self.assertEqual(encryption.encryption('haveaniceday'), 'hae and via ecy')
    self.assertEqual(encryption.encryption('feedthedog'), 'fto ehg ee dd')
    self.assertEqual(encryption.encryption('chillout'), 'clu hlt io')


if __name__ == '__main__':
  unittest.main()
