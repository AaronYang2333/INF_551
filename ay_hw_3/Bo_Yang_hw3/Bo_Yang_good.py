# 
__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '10/23/2019 9:47 PM'

HOST = '127.0.0.1'
USER = 'inf551'
PASSWORD = 'inf551'
DB = 'inf551'

import sys
import mysql.connector


def getConnection(host, user, pwd, db):
	connection = mysql.connector.connect(
		host=host,
		user=user,
		passwd=pwd,
		database=db
	)
	return connection


def executeQuery(connection, sql):
	result = list()
	cursor = connection.cursor()
	cursor.execute(sql)
	for facility_name in cursor:
		result.append(facility_name[0])

	cursor.close()
	return result

def dataToFile(data, file_path):
	output_file = open(file_path, "w+")
	for item in range(len(data)):
		output_file.write("{}\n".format(data[item]))

	output_file.close()

if __name__ == "__main__":
	output_file_path = sys.argv[1]
	# output_file_path = './output_file_name.txt'
	connection = getConnection(HOST, USER, PASSWORD, DB)

	sql = "SELECT DISTINCT(a.facility_name) FROM inspections a " \
		  "WHERE a.facility_id NOT IN ( " \
		  "SELECT DISTINCT (b.facility_id) FROM violations b" \
		  ") ORDER BY a.facility_name"

	name_list = executeQuery(connection, sql)
	connection.close()
	dataToFile(name_list, output_file_path)
