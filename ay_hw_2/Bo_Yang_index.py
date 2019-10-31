#
__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '10/9/2019 8:19 PM'

import sys
import copy
import re
from xml.dom import minidom
from xml.etree import ElementTree as ET

SELECTED_TAG = ['book', 'author', 'title', 'genre', 'description']


def create_or_get_element(parentNode, newNodeName, attrib={}, key=None):
	if None == parentNode:
		return ET.Element(newNodeName, attrib=attrib)
	else:
		nodelist = parentNode.findall("./" + newNodeName + "[@key=\"{}\"]".format(key))
		if None == nodelist or len(nodelist) == 0:
			newNode = ET.Element(newNodeName, attrib=attrib)
			parentNode.append(newNode)
			return newNode
		else:
			return (nodelist[0])


def wrapper(raw_str):
	raw_str = re.sub("[^\w\d'\s]+", '', raw_str)
	return raw_str.lower().split()


def gen_inverted_index(input_root_element, output_root_element):
	bookStack = []
	for node in input_root_element.iter():
		if node.tag in SELECTED_TAG:
			if node.tag == 'book':
				bookStack.clear()
				infoNode = create_or_get_element(None, "info", attrib=node.attrib)
				bookStack.append(infoNode)
			else:
				keywords_list = wrapper(node.text)
				infoNode = copy.deepcopy(bookStack[0])
				for keyword in keywords_list:
					keywordNode = create_or_get_element(output_root_element, "keyword", {"key": keyword}, key=keyword)
					infoNode.set("where", node.tag)
					keywordNode.append(infoNode)

	return output_root_element


def prettify(root_element):
	"""Return a pretty-printed XML string based on the Element.
	"""
	rough_string = ET.tostring(root_element, 'utf-8')
	reparsed = minidom.parseString(rough_string)
	return reparsed.toprettyxml(indent="\t")


def read_file_get_root_node(file_path):
	input_tree = ET.parse(file_path)
	return input_tree.getroot()


def export_xml(output_file_path, root_element):
	str_xml = prettify(root_element)
	myfile = open(output_file_path, "w")
	myfile.write(str_xml)


if __name__ == "__main__":
	input_file_path = sys.argv[1]
	output_file_path = sys.argv[2]
	# input_file_path = './assets/books.xml'
	# output_file_path = './index.xml'

	# read file
	input_root = read_file_get_root_node(input_file_path)

	# create a output xml file's root node
	output_root = create_or_get_element(None, "index")

	# generate inverted index
	output_root = gen_inverted_index(input_root, output_root)

	# write a output xml file
	export_xml(output_file_path, output_root)
