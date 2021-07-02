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

	# change it to whatever your path is (windows specific)
	#pathToJSONDataFiles = "D:/Downloads/notes n stuff/CODING/CIT/cit-gladys-project/JSON_FILES"

	

    # TODO: move somewhere so we need to read only once
	pathToJSONDataFiles = "D:/Downloads/notes n stuff/CODING/CIT/cit-gladys-project/JSON_FILES"
	data = readSat(sat, pathToJSONDataFiles) #first instance of putting stuff into data

	ddata ={}
	for obj in data:
		if obj['x'] not in ddata:
			ddata[obj['x']] = {}
		if obj['y'] not in ddata[obj['x']]:
			ddata[obj['x']][obj['y']] = obj['value']
	try:
		value = ddata[x][y]
	except:
		value = 0
	print(value)
	return value
