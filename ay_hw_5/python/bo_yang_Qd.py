#
from operator import add

from pyspark.shell import sqlContext

__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '11/28/2019 4:31 PM'

import sys
from pyspark import SparkContext

if __name__ == "__main__":
	# input_file_1_path = "likes.csv"
	# input_file_2_path = "frequents.csv"
	# input_file_3_path = "sells.csv"
	# output_file_path = "output.txt"
	input_file_1_path = sys.argv[1]
	input_file_2_path = sys.argv[2]
	input_file_3_path = sys.argv[3]
	output_file_path = sys.argv[4]
	sc = SparkContext.getOrCreate()

	like_lines = sc.textFile(input_file_1_path)
	fre_lines = sc.textFile(input_file_2_path)
	sells_lines = sc.textFile(input_file_3_path)

	result = fre_lines.map(lambda row: (row.split(',')[1], row.split(',')[0])) \
		.join(sells_lines.map(lambda row: (row.split(',')[0], row.split(',')[1]))) \
		.map(lambda row: row[1]) \
		.intersection(like_lines.map(lambda row: (row.split(',')[0], row.split(',')[1])))\
		.map(lambda row: row[0] + "\t" + row[1] + "\n").collect()

	output_file = open(output_file_path, "w+")
	output_file.writelines("Drinker\tBeer\n")
	output_file.writelines(result)
	output_file.close()
