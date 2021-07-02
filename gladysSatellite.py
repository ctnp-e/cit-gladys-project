import io
import json

"""
     Student: Mary Ivanov, Avyuktha Mattupalli
     Module: gladysSatellite
     Description: This module does satellite stuff
"""

#DO NOT CHANGE
def readSat(sat, pathToJSONDataFiles):
	"""
		reads satellite data from a json file
		Students do NOT need to change the readSat function.
	"""

	# data file path
	fileName = sat + "-satellite.json"
	filePath = pathToJSONDataFiles + "/" + fileName

	# open the file
	try:
		fileHandle = open(filePath)
	except IOError:
		print("ERROR: Unable to open the file " + filePath)
		raise IOError

	# print("filePath = ", filePath)

	# read the file
	data = json.load(fileHandle)

	return data


def gpsValue(x, y, sat):
	"""
		Reads the altitude, and time information into data structures "data".
		Returns the data that was read to the gladysUserInterface module
	"""

	#change it to whatever your path is (windows specific)
	pathToJSONDataFiles = "D:/Downloads/notes n stuff/CODING/CIT/cit-gladys-project/JSON_FILES"

	# read the satellite data
	data = readSat("altitude", pathToJSONDataFiles) #first instance of putting stuff into data
	data.append(readSat("time", pathToJSONDataFiles)) #also puts time into "data"

	# Returns the data that was read

	#data is essentially just an array of arrays.
	#to retrieve one element you do data[x][y] to retrieve a certain portion of a certain array.
	#arrays are sorted as x: y: value: so to retrieve for example the value of the index'd 3rd data set
	#you would simply do data[3][2]
	value = data
	return value
