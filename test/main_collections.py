# 
__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '9/6/2019 3:55 PM'

if __name__ == "__main__":
	# Python有五个标准的数据类型： 1.Numbers（数字） 2.String（字符串） 3.List（列表） 4.Tuple（元组） 5.Dictionary（字典）
	dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 8: 10}  # 字典是无序的对象集合
	print(type(dict1))
	print(dict1.get('g'))  # None
	# C
	print("dict1.items() --> ", dict1.items())
	dict1['j'] = 9
	print(dict1)
	print(dict1.fromkeys(dict1))  # {'a': None, 'b': None, 'c': None, 'd': None, 'e': None}
	print(dict1.fromkeys(dict1, 1))  # {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1}
	# R
	print(dict1.get('a'))
	print(dict1['a'])
	# U
	dict1['a'] = 8
	dict1.update({'b': 10})
	dict1.update({'f': 10})
	print(dict1)
	# D
	print(dict1.popitem())  # ('f', 10)
	print(dict1.pop('b'))  # 10
	print(dict1)
	dict1.clear()

	# dict1.
	# --------------------------------------------------------------------------
	print("# --------------------------------------------------------------------------")
	list1 = [1, 2, 3, 4, 5]  # 列表是有序的对象集合
	print(type(list1))
	# C
	list1.append(9)
	list1.append(None)
	list1.insert(0, 8)
	print("C - - > ", list1)
	# D
	list1.pop()  # Remove and return item at index (default last).
	list1.remove(2)  # Remove first occurrence of value "not index"
	print("D - - > ", list1)
	# U
	list1[0] = 0
	print("U - - > ", list1)
	# R
	print(list1.index(4))  # Return first index of value.
	print(list1[1:3])

	list2 = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
	print(type(list2))
	# --------------------------------------------------------------------------
	print("# --------------------------------------------------------------------------")

	tuple1 = ({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}, 22, True)  # 元组不能二次赋值，相当于只读列表。
	print(type(tuple1))
	# C 不能增加 只能连接一个新的元祖
	tuple2 = (12, 34.56)
	print(tuple1 + tuple2)
	# tuple2.append('33') # AttributeError: 'tuple' object has no attribute 'append'
	print(tuple2)
	# R
	print(tuple2[0])
