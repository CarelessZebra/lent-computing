"""This is a module that does stuff
"""
from .utils import sorted_by_key
def stations_level_over_threshold(stations, tol):
    """returns a list of tuples, where each tuple holds (i) a station (object) at which the latest relative water level is over 
    tol and (ii) the relative water level at the station. The returned list of tuples is sorted by the latest relative water level in descending order."""
    #create empty list
    stations_levels_over_threshold = []
    #iterate through stations
    for station in stations:
        #check that the data is consistent
        if station.relative_water_level() != None:
            #check if relative water level is higher than the tolerance
            if station.relative_water_level() > tol:
                #add the station and the relative water level in a tuple to the list
                stations_levels_over_threshold.append((station, station.relative_water_level()))
                #sort by relative water level descending
                stations_levels_over_threshold = sorted_by_key(stations_levels_over_threshold, 1, True)
    return stations_levels_over_threshold

