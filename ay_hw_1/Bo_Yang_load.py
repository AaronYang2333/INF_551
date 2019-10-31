# 
__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '9/12/2019 10:01 AM'

import sys
import json
import requests
import pandas as pd
import urllib.parse

RESTAURANTS = 'restaurants'
INDEX = 'index'
FACILITY_NAME = 'facility_name'
SERIAL_NUMBER = 'serial_number'
SLASH = '/'

baseURL = 'https://ay2333.firebaseio.com/hw1'
json_suffix = '.json'
columns = ['serial_number', 'facility_name', 'score']


def load_content_by_columns(path, columns):
	# load data from csv file into json format
	dataFrame = pd.read_csv(path, usecols=columns, low_memory=False)
	json = dataFrame.to_json(orient='records')
	return '{"' + RESTAURANTS + '": ' + json + '}'


def truncate_db(url):
	try:
		delResponse = requests.delete(url + json_suffix)
		if delResponse.status_code == 200:
			print("Truncate firebase Successfully")
		else:
			print("Truncate DB failed, Reason: {}".format(delResponse.text))
	except:
		print("Truncate DB failed")


def upload_data(url, data, tips='data'):
	try:
		putResponse = requests.put(url + json_suffix, data)
		if putResponse.status_code == 200:
			print("Upload {} Successfully".format(tips))
		else:
			print("Upload data failed, Reason: {}".format(putResponse.text))
	except:
		print("Upload {} failed".format(tips))


def encode(str):
	return urllib.parse.quote(str, safe='').replace('.', '%2e')


def create_index(data):
	result = {}
	nameSet = set()
	for item in data:
		for name in ' '.join(item[FACILITY_NAME].lower().split()).split(' '):
			if name in nameSet:
				result.get(encode(name)).append(item[SERIAL_NUMBER])
			else:
				nameSet.add(name)
				result.setdefault(encode(name), [item[SERIAL_NUMBER]])

	return result


def query_data(path):
	getURL = baseURL + SLASH + path + json_suffix
	response = requests.get(getURL)
	return json.loads(response.text)


if __name__ == "__main__":
	assert len(sys.argv[1]) > 1, "Please input a valid csv file name"
	filePath = sys.argv[1]
	print(filePath)
	# filePath = './assets/{}.csv'.format(RESTAURANTS)
	print("You are going to upload {} into firebase".format(filePath))

	# load file content by file path and assigned columns
	fileContent = load_content_by_columns(filePath, columns)
	print("Going to truncate aaron's firebase ....")
	# truncate DB and then insert all
	truncate_db(baseURL)
	print("Going to upload data to aaron's firebase ....")
	upload_data(baseURL, fileContent, tips='json')

	# get Data from firebase
	jsonData = query_data(RESTAURANTS)

	# convert into inverted index
	invertedIndex = create_index(jsonData)
	print(json.dumps(invertedIndex, indent=4))

	# save the index into firebase
	print("Going to upload index to aaron's firebase ....")
	upload_data(baseURL + SLASH + INDEX, json.dumps(invertedIndex), tips='index')
