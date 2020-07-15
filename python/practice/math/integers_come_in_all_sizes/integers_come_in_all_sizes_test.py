import unittest, integers_come_in_all_sizes


class TestIntegersComeInAllSizes(unittest.TestCase):
  def test_integers_come_in_all_sizes(self):
    self.assertEqual(
        integers_come_in_all_sizes.integers_come_in_all_sizes(9, 29, 7, 27),
        4_710_194_409_608_608_369_201_743_232)


if __name__ == '__main__':
  unittest.main()
