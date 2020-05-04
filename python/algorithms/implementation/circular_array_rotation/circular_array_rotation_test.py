import unittest, circular_array_rotation


class TestCircularArrayRotation(unittest.TestCase):
  def test_circular_array_rotation(self):
    self.assertEqual(
        circular_array_rotation.circular_array_rotation([1, 2, 3], 2,
                                                        [0, 1, 2]), [2, 3, 1])


if __name__ == '__main__':
  unittest.main()
