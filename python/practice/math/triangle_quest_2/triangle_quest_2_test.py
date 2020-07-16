from io import StringIO
from unittest.mock import patch
import unittest, triangle_quest_2


class TestTriangleQuest2(unittest.TestCase):
  def test_triangle_quest_2(self):
    with patch('sys.stdout', new=StringIO()) as fake_out:
      triangle_quest_2.triangle_quest_2(5)
      self.assertEqual(fake_out.getvalue(), '''1
121
12321
1234321
123454321
''')


if __name__ == '__main__':
  unittest.main()
