import unittest, marcs_cakewalk


class TestMarcsCakewalk(unittest.TestCase):
  def test_marcs_cakewalk(self):
    self.assertEqual(marcs_cakewalk.marcs_cakewalk([1, 3, 2]), 11)
    self.assertEqual(marcs_cakewalk.marcs_cakewalk([7, 4, 9, 6]), 79)


if __name__ == '__main__':
  unittest.main()
