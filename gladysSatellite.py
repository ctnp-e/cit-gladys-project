import io
import json

"""
     Student: Mary Ivanov, Avyuktha Mattupalli
     Module: gladysSatellite
     Description: This module does satellite stuff
"""

data = {
	'altitude': None,
	'latitude': None,
	'longitude': None,
	'time': None,
}

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

	# read the file
	data = json.load(fileHandle)

	return data

def loadData():
	"""
		Loads the altitude, and time information into data structures "data".
	"""

	for dim in [ "altitude", "latitude", "longitude", "time"]:
		converted = dict()
		for d in readSat(dim, "data"):
			if d['x'] not in converted:
				converted[d['x']] = dict()
			converted[d['x']][d['y']] = d['value']
		data[dim] = converted

def gpsValue(x, y, sat):
	"""
		Reads the altitude, and time information into data structures "data".
		Returns the data that was read to the gladysUserInterface module
	"""
	return data[sat][x][y]
