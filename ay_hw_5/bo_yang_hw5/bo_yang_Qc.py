#
from operator import add

from pyspark.shell import sqlContext

__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '11/28/2019 4:31 PM'

import sys
from pyspark import SparkContext

if __name__ == "__main__":
	# input_file_1_path = "frequents.csv"
	# input_file_2_path = "likes.csv"
	# output_file_path = "output.txt"
	input_file_1_path = sys.argv[1]
	input_file_2_path = sys.argv[2]
	output_file_path = sys.argv[3]
	sc = SparkContext.getOrCreate()

	fre_lines = sc.textFile(input_file_1_path)
	like_lines = sc.textFile(input_file_2_path)
	result = fre_lines.map(lambda row: row.split(',')[0]).distinct() \
		.subtract(like_lines.map(lambda row: row.split(',')[0]).distinct()) \
		.map(lambda row: str(row) + "\n").collect()

	#
	output_file = open(output_file_path, "w+")
	output_file.writelines("Drinker\n")
	output_file.writelines(result)
	output_file.close()
