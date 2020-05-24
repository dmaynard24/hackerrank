import unittest, intro_tutorial


class TestIntroTutorial(unittest.TestCase):
  def test_intro_tutorial(self):
    self.assertEqual(intro_tutorial.intro_tutorial(4, [1, 4, 5, 7, 9, 12]), 1)


if __name__ == '__main__':
  unittest.main()
