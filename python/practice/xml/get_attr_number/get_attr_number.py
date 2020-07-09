import xml.etree.ElementTree as etree


def get_attr_number(node):
  return sum([len(el.attrib) for el in node.iter()])