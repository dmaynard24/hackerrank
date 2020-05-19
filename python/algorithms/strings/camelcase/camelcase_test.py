import unittest, camelcase


class TestCamelcase(unittest.TestCase):
  def test_camelcase(self):
    self.assertEqual(camelcase.camelcase('saveChangesInTheEditor'), 5)


if __name__ == '__main__':
  unittest.main()
