import unittest, sequence_equation


class TestSequenceEquation(unittest.TestCase):
  def test_sequence_equation(self):
    self.assertEqual(sequence_equation.sequence_equation([2, 3, 1]), [2, 3, 1])
    self.assertEqual(sequence_equation.sequence_equation([4, 3, 5, 1, 2]),
                     [1, 3, 5, 4, 2])
    self.assertEqual(sequence_equation.sequence_equation([5, 3, 4, 1, 2]),
                     [3, 1, 5, 2, 4])


if __name__ == '__main__':
  unittest.main()
