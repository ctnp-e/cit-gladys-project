import io
import math
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
    
    #Get coordinates from data returned by gpsValue
    latitude = satellite.gpsValue(x, y, "latitude")[0][0]
    longtitude = satellite.gpsValue(x, y, "longtitude")[0][0]
    altitude = satellite.gpsValue(x, y, "altitude")[0][0]
    time = satellite.gpsValue(x, y, "time")[0][0]
    
    #Compute average
    average = (latitude + longtitude + altitude + time) / 4

    return average

# end of the code by Minh Le

#Start of code by Hubert Pham
def distance(current, dest):
    
    #initialize variables
    aveg1 = 0
    aveg2 = 0
    distance = 0

    aveg1 = math.pow(gpsAverage(current[0], current[1]), 2)
    aveg2 = math.pow(gpsAverage(dest[0], dest[1], ), 2)
    distance = math.sqrt(aveg1 + aveg2 )
    return distance