from io import StringIO
from unittest.mock import patch
import unittest, triangle_quest


class TestTriangleQuest(unittest.TestCase):
  def test_triangle_quest(self):
    with patch('sys.stdout', new=StringIO()) as fake_out:
      triangle_quest.triangle_quest(5)
      self.assertEqual(fake_out.getvalue(), '''1
22
333
4444
''')


if __name__ == '__main__':
  unittest.main()
