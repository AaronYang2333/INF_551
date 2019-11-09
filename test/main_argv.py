# 
__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '10/9/2019 8:14 PM'
import sys

if __name__ == "__main__":
	assert len(sys.argv[1]) > 1, "Please input a valid csv file name"
	filePath = sys.argv[1]
	print(filePath)