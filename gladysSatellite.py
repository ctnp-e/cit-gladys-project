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
	pathToJSONDataFiles = "C:/Users/jerom/GitHub/evc-cit134a-python/gladys-west-map/data"

	# read the satellite data
	data = readSat("altitude", pathToJSONDataFiles) #first instance of putting stuff into data
	data.append(readSat("time", pathToJSONDataFiles)) #also puts time into "data"

	# Returns the data that was read
	value = data
	return value
