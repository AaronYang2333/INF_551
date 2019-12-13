#
from operator import add

__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '11/28/2019 4:31 PM'

import sys
from pyspark import SparkContext


def splitFunc(row):
	col_bar, col_beer, col_price = row.split(',')
	if col_beer.startswith('Bud'):
		return col_bar, int(col_price)


if __name__ == "__main__":
	# input_file_path = "sells.csv"
	# output_file_path = "output.txt"
	# input_file_path = sys.argv[1]
	# output_file_path = sys.argv[2]
	d = [('hello', 1), ('world', 1), ('hello', 1), ('this', 1), ('world', 1)]
	sc = SparkContext.getOrCreate()
	data = sc.parallelize(d, 2)
	# ss = data.countByKey()

	ss = data.reduceByKey(add).collect()

	print(ss)


