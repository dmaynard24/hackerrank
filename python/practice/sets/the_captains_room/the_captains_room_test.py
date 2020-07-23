import unittest, the_captains_room


class TestTheCaptainsRoom(unittest.TestCase):
  def test_the_captains_room(self):
    self.assertEqual(
        the_captains_room.the_captains_room(5, [
            1, 2, 3, 6, 5, 4, 4, 2, 5, 3, 6, 1, 6, 5, 3, 2, 4, 1, 2, 5, 1, 4,
            3, 6, 8, 4, 3, 1, 5, 6, 2
        ]), 8)


if __name__ == '__main__':
  unittest.main()
