#
from operator import add

__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '11/28/2019 4:31 PM'

import sys
from pyspark import SparkContext

if __name__ == "__main__":
	# input_file_path = "sells.csv"
	# output_file_path = "output.txt"
	input_file_path = sys.argv[1]
	output_file_path = sys.argv[2]
	sc = SparkContext.getOrCreate()

	lines = sc.textFile(input_file_path)
	result = lines.map(lambda row: (row.split(',')[0], int(row.split(',')[2]))) \
		.aggregateByKey((0, 0), lambda a, b: (a[0] + b, a[1] + 1), lambda a, b: (a[0] + b[0], a[1] + b[1])) \
		.map(lambda row: str(row[0]) + "\t" + str(row[1][0] / row[1][1]) + "\n").collect()

	output_file = open(output_file_path, "w+")
	output_file.writelines("Bar\t\tAverage_price\n")
	output_file.writelines(result)
	output_file.close()
