import unittest, tuple_hash


class TestTupleHash(unittest.TestCase):
  def test_tuple_hash(self):
    self.assertEqual(tuple_hash.tuple_hash([1, 2]), 3713081631934410656)
    self.assertEqual(
        tuple_hash.tuple_hash([
            387, 38, 498, 988, 434, 282, 467, 641, 464, 682, 341, 586, 222,
            736, 187, 415, 330, 323, 109, 818, 78, 469, 560, 623, 748, 782,
            352, 398, 196, 39, 603, 344, 630, 841, 794, 994, 648, 293, 861,
            800, 944, 249, 921, 10, 781, 437, 915, 451, 782, 262
        ]), 8113509743655314852)


if __name__ == '__main__':
  unittest.main()
