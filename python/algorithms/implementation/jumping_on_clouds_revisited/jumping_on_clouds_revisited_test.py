import unittest, jumping_on_clouds_revisited


class TestJumpingOnCloudsRevisited(unittest.TestCase):
  def test_jumping_on_clouds_revisited(self):
    self.assertEqual(
        jumping_on_clouds_revisited.jumping_on_clouds_revisited(
            [0, 0, 1, 0, 0, 1, 1, 0], 2), 92)
    self.assertEqual(
        jumping_on_clouds_revisited.jumping_on_clouds_revisited(
            [1, 1, 1, 0, 1, 1, 0, 0, 0, 0], 3), 80)


if __name__ == '__main__':
  unittest.main()
