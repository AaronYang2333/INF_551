# 
__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '9/6/2019 3:45 PM'

import json


if __name__ == "__main__":
	data = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
	print(type(data))  # <class 'list'>
	# json.dumps 用于将 Python 对象编码成 JSON 字符串
	jsonStr = json.dumps(data)
	print(jsonStr)  # <class 'str'>

	jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":{"1":23}}'

	dict_obj = json.loads(jsonData)
	print(dict_obj)
	print(type(dict_obj))

	# keys must be str, int, float, bool or None, not tuple
	# print(json.dumps({(1,2): 3}))
	# Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
	#print(json.loads("{'1': 3}"))
	# Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
	# print(json.loads('{(1): 3}'))
	# Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
	# print(json.loads('{1: 3}'))

	print(json.loads('{"1": 3}'))
	import urllib.parse
	# str = 'l.a.a.c.-8th'
	str = "HOUSE  OF  CURRY"
	list = ' '.join(str.lower().split()).split(' ')
	# list = str.lower().split(' ')
	print(list)

