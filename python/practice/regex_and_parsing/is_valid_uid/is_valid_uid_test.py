import unittest, is_valid_uid


class TestIsValidUid(unittest.TestCase):
  def test_is_valid_uid(self):
    self.assertEqual(is_valid_uid.is_valid_uid('B1CD102354'), False)
    self.assertEqual(is_valid_uid.is_valid_uid('B1CDEF2354'), True)


if __name__ == '__main__':
  unittest.main()
