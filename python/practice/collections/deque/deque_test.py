import unittest, deque


class TestDeque(unittest.TestCase):
  def test_deque(self):
    self.assertEqual(
        deque.deque([
            'append 1', 'append 2', 'append 3', 'appendleft 4', 'pop',
            'popleft'
        ]), '1 2')


if __name__ == '__main__':
  unittest.main()