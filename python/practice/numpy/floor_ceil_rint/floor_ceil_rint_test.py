from io import StringIO
from unittest.mock import patch
import unittest, floor_ceil_rint


class TestFloorCeilRint(unittest.TestCase):
  def test_floor_ceil_rint(self):
    with patch('sys.stdout', new=StringIO()) as fake_out:
      floor_ceil_rint.floor_ceil_rint(
          [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
      self.assertEqual(
          fake_out.getvalue(), '''[1. 2. 3. 4. 5. 6. 7. 8. 9.]
[ 2.  3.  4.  5.  6.  7.  8.  9. 10.]
[ 1.  2.  3.  4.  6.  7.  8.  9. 10.]
''')


if __name__ == '__main__':
  unittest.main()
