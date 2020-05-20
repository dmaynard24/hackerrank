import unittest, mars_exploration


class TestMarsExploration(unittest.TestCase):
  def test_mars_exploration(self):
    self.assertEqual(mars_exploration.mars_exploration('SOSSOT'), 1)
    self.assertEqual(mars_exploration.mars_exploration('SOSSPSSQSSOR'), 3)
    self.assertEqual(mars_exploration.mars_exploration('SOSSOSSOS'), 0)


if __name__ == '__main__':
  unittest.main()
