import unittest, no_idea


class TestNoIdea(unittest.TestCase):
  def test_no_idea(self):
    self.assertEqual(no_idea.no_idea([1, 5, 3], {3, 1}, {5, 7}), 1)


if __name__ == '__main__':
  unittest.main()
