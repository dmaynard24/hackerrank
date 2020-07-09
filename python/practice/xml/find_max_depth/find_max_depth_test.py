import unittest, find_max_depth
import xml.etree.ElementTree as etree


class TestFindMaxDepth(unittest.TestCase):
  def test_find_max_depth(self):
    xml = '''<feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    <updated>2013-12-25T12:00:00</updated>
</feed>'''
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    self.assertEqual(find_max_depth.find_max_depth(root), 1)

  def test_find_max_depth_1(self):
    xml = '''<feed xml:lang='en'>
  <title>HackerRank</title>
  <subtitle lang='en'>Programming challenges</subtitle>
  <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
  <updated>2013-12-25T12:00:00</updated>
  <entry>
  	<author gender='male'>Harsh</author>
    <question type='hard'>XML 1</question>
    <description type='text'>This is related to XML parsing</description>
  </entry>
</feed>'''
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    self.assertEqual(find_max_depth.find_max_depth(root), 2)

  def test_find_max_depth_1(self):
    xml = '''<feed xml:lang='en'>
  <title>HackerRank</title>
  <subtitle lang='en'>Programming challenges</subtitle>
  <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
  <updated>2013-12-25T12:00:00</updated>
  <entry>
  	<author gender='male'>Harsh</author>
    <question type='hard'>XML 1</question>
    <description type='text'>This is related to XML parsing</description>
  </entry>
</feed>'''
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    self.assertEqual(find_max_depth.find_max_depth(root), 2)

  def test_find_max_depth_2(self):
    xml = '''<feed xml:lang='en'>
	<subfeed>
    	<super>
        	<sub>
            	This is it
            </sub>
        </super>
    </subfeed>
</feed>'''
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    self.assertEqual(find_max_depth.find_max_depth(root), 3)


if __name__ == '__main__':
  unittest.main()