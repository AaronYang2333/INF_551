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
	input_file_path = "../assets/sells.csv"
	output_file_path = "./output.txt"
	# input_file_path = sys.argv[1]
	# output_file_path = sys.argv[2]
	sc = SparkContext.getOrCreate()

	lines = sc.textFile(input_file_path)

	result = lines.map(splitFunc) \
		.filter(lambda row: row is not None) \
		.mapValues(lambda value: 1 if value <= 5 else 0) \
		.reduceByKey(add) \
		.map(lambda row: str(row[0]) + "\t" + str(row[1]) + "\n").collect()


	output_file = open(output_file_path, "w+")
	output_file.writelines(result)
	output_file.close()
