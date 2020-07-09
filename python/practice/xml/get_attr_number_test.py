import unittest, get_attr_number
import xml.etree.ElementTree as etree


class TestGetAttrNumber(unittest.TestCase):
  def test_get_attr_number(self):
    xml = '''<feed xml:lang='en'>
  <title>HackerRank</title>
  <subtitle lang='en'>Programming challenges</subtitle>
  <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
  <updated>2013-12-25T12:00:00</updated>
</feed>'''
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    self.assertEqual(get_attr_number.get_attr_number(root), 5)

  def test_get_attr_number_1(self):
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
    self.assertEqual(get_attr_number.get_attr_number(root), 8)


if __name__ == '__main__':
  unittest.main()