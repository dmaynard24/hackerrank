import unittest, jumping_on_clouds


class TestJumpingOnClouds(unittest.TestCase):
  def test_jumping_on_clouds(self):
    self.assertEqual(
        jumping_on_clouds.jumping_on_clouds([0, 0, 1, 0, 0, 1, 0]), 4)

  def test_jumping_on_clouds_1(self):
    self.assertEqual(jumping_on_clouds.jumping_on_clouds([0, 0, 0, 0, 1, 0]),
                     3)


if __name__ == '__main__':
  unittest.main()
