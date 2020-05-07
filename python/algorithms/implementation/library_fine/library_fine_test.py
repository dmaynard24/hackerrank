import unittest, library_fine


class TestLibraryFine(unittest.TestCase):
  def test_library_fine(self):
    self.assertEqual(library_fine.library_fine(9, 6, 2015, 6, 6, 2015), 45)


if __name__ == '__main__':
  unittest.main()
