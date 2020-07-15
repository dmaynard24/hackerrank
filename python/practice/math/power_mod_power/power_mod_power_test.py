from io import StringIO
from unittest.mock import patch
import unittest, power_mod_power


class TestPowerModPower(unittest.TestCase):
  def test_power_mod_power(self):
    with patch('sys.stdout', new=StringIO()) as fake_out:
      power_mod_power.power_mod_power(3, 4, 5)
      self.assertEqual(fake_out.getvalue(), '''81
1
''')


if __name__ == '__main__':
  unittest.main()
