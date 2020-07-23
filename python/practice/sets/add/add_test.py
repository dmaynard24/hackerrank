import unittest, add


class TestAdd(unittest.TestCase):
  def test_add(self):
    self.assertEqual(
        add.add(
            ['UK', 'China', 'USA', 'France', 'New Zealand', 'UK', 'France']),
        5)


if __name__ == '__main__':
  unittest.main()
