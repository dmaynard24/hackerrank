import unittest, match_specific_string


class TestMatchSpecificString(unittest.TestCase):
  def test_match_specific_string(self):
    self.assertEqual(
        match_specific_string.match_specific_string(
            'The hackerrank team is on a mission to flatten the world by restructuring the DNA of every company on the planet. We rank programmers based on their coding skills, helping companies source great programmers and reduce the time to hire. As a result, we are revolutionizing the way companies discover and evaluate talented engineers. The hackerrank platform is the destination for the best engineers to hone their skills and companies to find top engineers.',
            'hackerrank'), 'Number of matches : 2')


if __name__ == '__main__':
  unittest.main()
