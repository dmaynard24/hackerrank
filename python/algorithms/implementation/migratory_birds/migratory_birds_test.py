import unittest, migratory_birds


class TestMigratoryBirds(unittest.TestCase):
  def test_migratory_birds(self):
    self.assertEqual(migratory_birds.migratory_birds([1, 4, 4, 4, 5, 3]), 4)
    self.assertEqual(
        migratory_birds.migratory_birds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]), 3)


if __name__ == '__main__':
  unittest.main()
