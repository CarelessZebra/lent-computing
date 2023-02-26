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

def stations_highest_rel_level(stations, N):
    """Returns list of N stations sorted in descending order by relative level"""
    #get list of all the stations sorted by relative water level descending
    stations_levels = stations_level_over_threshold(stations, -100000)
    station_list = []
    count = 0
    for station, level in stations_levels:
        #add station to station list
        station_list.append(station)
        count += 1
        #when N stations have been added to the list return the list
        if count >= N:
            return station_list
        
    #should probably have a separate return for if N is greater
    #than the number of stations but python lets me get away with this.



    