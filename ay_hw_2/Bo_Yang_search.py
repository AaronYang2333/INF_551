#

__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '10/9/2019 8:24 PM'

import re
import sys
from xml.etree import ElementTree as ET

from lxml import etree

SELECTED_TAG = ['book', 'author', 'title', 'genre', 'description']


def prettify(root_element):
	"""Return a pretty-printed XML string based on the Element.
	"""
	rough_string = ET.tostring(root_element, 'utf-8').decode("utf-8")
	parser = etree.XMLParser(remove_blank_text=True)
	test_root = etree.XML(rough_string, parser)
	return str(etree.tostring(test_root, pretty_print=True), 'utf-8')


def read_file_get_root_node(file_path):
	input_tree = ET.parse(file_path)
	return input_tree.getroot()


def export_xml(out_file_path, root_element):
	# prettify(root_element)
	str_xml = prettify(root_element)
	myfile = open(out_file_path, "w")
	myfile.write(str_xml)


def wrapper(raw_str):
	raw_str = re.sub("[^\w\d'\s]+", '', raw_str)
	return raw_str.lower().split()


def is_empty_or_none(itea_obj):
	return None == itea_obj or len(itea_obj) == 0


def search_by_keywords(keywords, index_root_element):
	search_result_info = []
	for keyword in keywords:
		temp = {}
		ky_node_list = index_root_element.findall("./keyword[@key=\"{}\"]".format(keyword))
		if not is_empty_or_none(ky_node_list):
			all_info_nodes = list(ky_node_list[0])
			for num, info in enumerate(all_info_nodes):
				if info.get('id') in temp:
					temp.get(info.get('id')).add(info.get('where'))
				else:
					temp.setdefault(info.get('id'), set([info.get('where')]))

		for key, value in temp.items():
			value = sorted(value, key=SELECTED_TAG.index)
			temp[key] = value
		search_result_info.append(temp)
	return search_result_info


def find_in_common(result_infos):
	results = {}
	keySet = None

	for index, info in enumerate(result_infos):
		if is_empty_or_none(keySet):
			keySet = set(info.keys())
		else:
			keySet = keySet & set(info.keys())

	for key in keySet:
		whereSet = None
		for index, info in enumerate(result_infos):
			if is_empty_or_none(whereSet):
				whereSet = set(info.get(key))
			else:
				whereSet = whereSet & set(info.get(key))

		results[key] = whereSet if len(whereSet) > 0 else {}

	return results


def traverse_searched_info(root_elemnt, results):
	for key, value in results.items():
		book_node = ET.Element('book', {"id": key})
		for value_item in list(value):
			node = original_data_root.findall("./book[@id=\"" + key + "\"]/{}".format(value_item))[0]
			book_node.append(node)
		root_elemnt.append(book_node)


def extract_elements(results, original_data_root):
	root = ET.Element('results')
	if is_empty_or_none(results):
		return root
	else:
		for key, value in results.items():
			book_node = ET.Element('book', {"id": key})
			for value_item in list(value):
				node = original_data_root.findall("./book[@id=\"" + key + "\"]/{}".format(value_item))[0]
				book_node.append(node)
			if len(list(book_node)) > 0:
				root.append(book_node)
		return root


if __name__ == "__main__":
	# original_data_file_path = sys.argv[1]
	# inverted_index_file_path = sys.argv[2]
	# keywords = sys.argv[3]
	# output_file_path = sys.argv[4]
	original_data_file_path = './assets/books.xml'
	inverted_index_file_path = './index.xml'
	keywords = "A"
	output_file_path = './results.xml'

	# read files
	original_data_root = read_file_get_root_node(original_data_file_path)
	index_root = read_file_get_root_node(inverted_index_file_path)

	# wrapper the keywords
	keyword_list = wrapper(keywords)

	result_infos = search_by_keywords(keyword_list, index_root)
	if len(keyword_list) > 1:
		results = find_in_common(result_infos)
	else:
		results = result_infos[0]

	output_root = extract_elements(results, original_data_root)
	# write a output xml file
	export_xml(output_file_path, output_root)
