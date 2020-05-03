import unittest, angry_professor


class TestAngryProfessor(unittest.TestCase):
  def test_angry_professor(self):
    self.assertEqual(angry_professor.angry_professor(3, [-1, -3, 4, 2]), 'YES')
    self.assertEqual(angry_professor.angry_professor(2, [0, -1, 2, 1]), 'NO')


if __name__ == '__main__':
  unittest.main()
