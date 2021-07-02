import io

import gladysSatellite as satellite

"""
	Student: Minh Le, Hubert Pham
	Module: gladysCompute
	Description: This module does compute program
"""
# start of code by Minh Le

def gpsAverage(x, y):
    """ 
    This function computes the GPS value average of a position by taking a GPS value and dividing by 2 
    """
 
    value = satellite.gpsValue(x, y, "altitude")

    average = value / 2

    return average



def distance(current, destination):

	"""
	This function calculates the distance between two positions by multiply their GPS average with each other
	"""
	
	distance = gpsAverage(current['x'], current['y']) * gpsAverage(destination['x'], destination['y'])
	
	return distance

	
# end of the code by Minh Le