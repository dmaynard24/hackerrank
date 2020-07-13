import unittest, eye_and_identity


class TestEyeAndIdentity(unittest.TestCase):
  def test_eye_and_identity(self):
    self.assertEqual(eye_and_identity.eye_and_identity(3, 3), '''[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]''')


if __name__ == '__main__':
  unittest.main()