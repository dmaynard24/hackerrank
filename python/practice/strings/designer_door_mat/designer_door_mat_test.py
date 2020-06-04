import unittest, designer_door_mat


class TestDesignerDoorMat(unittest.TestCase):
  def test_designer_door_mat(self):
    self.assertEqual(designer_door_mat.designer_door_mat(9, 27), [
        '------------.|.------------', '---------.|..|..|.---------',
        '------.|..|..|..|..|.------', '---.|..|..|..|..|..|..|.---',
        '----------WELCOME----------', '---.|..|..|..|..|..|..|.---',
        '------.|..|..|..|..|.------', '---------.|..|..|.---------',
        '------------.|.------------'
    ])


if __name__ == '__main__':
  unittest.main()
