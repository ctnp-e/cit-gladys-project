import io

import gladysSatellite as satellite

"""
	Student: Minh Le, Hubert Pham
	Module: gladysCompute
	Description: This module does compute program
"""
# start of code by Minh Le

def gpsAverage(place):
    """ 
    This function computes the GPS value average of a position by taking a GPS value and dividing by 2 
    """
	
    value = satellite.gpsValue(place[0], place[1], "latitude")
    
    average = value / 2
    print(average)
    return average

# end of the code by Minh Le

def distance(current, destination):
	"""
		calculates distance
	"""
	distance = gpsAverage(current) * gpsAverage(destination)

	return distance

# end of distance by Mary Ivanov