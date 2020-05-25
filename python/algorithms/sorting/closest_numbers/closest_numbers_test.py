import unittest, closest_numbers


class TestClosestNumbers(unittest.TestCase):
  def test_closest_numbers(self):
    self.assertEqual(
        closest_numbers.closest_numbers([
            -20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457,
            -6461594, 266854
        ]), [-20, 30])
    self.assertEqual(closest_numbers.closest_numbers([-5, 15, 25, 71, 63]),
                     [63, 71])
    self.assertEqual(closest_numbers.closest_numbers([5, 4, 3, 2]),
                     [2, 3, 3, 4, 4, 5])


if __name__ == '__main__':
  unittest.main()
