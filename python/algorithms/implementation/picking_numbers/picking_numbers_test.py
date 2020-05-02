import unittest, picking_numbers


class TestPickingNumbers(unittest.TestCase):
  def test_picking_numbers(self):
    self.assertEqual(picking_numbers.picking_numbers([4, 6, 5, 3, 3, 1]), 3)
    self.assertEqual(picking_numbers.picking_numbers([1, 2, 2, 3, 1, 2]), 5)


if __name__ == '__main__':
  unittest.main()
