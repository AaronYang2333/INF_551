# 
__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '9/12/2019 10:01 AM'

import sys
import json
import requests
import urllib.parse

RESTAURANTS = 'restaurants'
INDEX = 'index'
FACILITY_NAME = 'facility_name'
SERIAL_NUMBER = 'serial_number'
SCORE = 'score'
SLASH = '/'

baseURL = 'https://ay2333.firebaseio.com/hw1'
json_suffix = '.json'
columns = ['serial_number', 'facility_name', 'score']


def query_data(path):
	getURL = baseURL + SLASH + path + json_suffix
	response = requests.get(getURL)
	return json.loads(response.text)


def encode(str):
	return urllib.parse.quote(str, safe='').replace('.', '%2e')


def get_unique_ids(keywords, indexData):
	temp_list = []
	for keyword in keywords:
		temp_list.extend(indexData[encode(keyword)])

	return list(set(temp_list))


def retrieve_result(ids, data):
	result = {}
	print("{")
	for id in ids:
		for item in data:
			if id == item[SERIAL_NUMBER]:
				result.setdefault(id, {FACILITY_NAME: item[FACILITY_NAME], SCORE: item[SCORE]})
				print("    \"{}\": {{ \"facility_name\": \"{}\", \"score\": {} }},".format(
					id, item[FACILITY_NAME], item[SCORE]))
				break


if __name__ == '__main__':
	assert len(sys.argv[1]) > 1, "Please input a valid keyword string"
	keywords = ' '.join(sys.argv[1].lower().split()).split(' ')
	print("You are going to search restaurants with these following keywords :", keywords)

	# inputStr = "coffee "
	# keywords = ' '.join(inputStr.lower().split()).split(' ')

	print("Retrieving the inverted index data from aaron's firebase ...")
	# get the index data from firebase
	indexData = query_data(INDEX)

	# get all related restaurants ids
	serialNumberList = get_unique_ids(keywords, indexData)

	print("Retrieving the restaurants data from aaron's firebase ...")
	jsonData = query_data(RESTAURANTS)

	print("Execute your searching ... ")
	retrieve_result(serialNumberList, jsonData)
	# print(json.dumps(result, indent=2))
	print("}")
