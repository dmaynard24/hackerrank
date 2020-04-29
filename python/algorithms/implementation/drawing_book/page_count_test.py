import unittest, page_count


class TestPageCount(unittest.TestCase):
  def test_page_count(self):
    self.assertEqual(page_count.page_count(6, 2), 1)
    self.assertEqual(page_count.page_count(5, 4), 0)


if __name__ == '__main__':
  unittest.main()
