# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from haversine import haversine
from .utils import sorted_by_key  # noqa

def stations_within_radius(stations, centre, r):
    """Build and return a list of all stations, type MonitoringStations, within a specified radius r around a coordinate centre"""
    stations_in_radius = []
    #iterate through the stations
    for station in stations:
        #calculate distance from centre coord to station coord
        distance = haversine(station.coord, centre)
        #add station to list of stations in radius if its distance to the centre is less than or equal to the radius
        if distance <= r:
            stations_in_radius.append(station)
    return stations_in_radius

def rivers_with_station(stations):
    """Builds and returns a set of unique rivers from a list of MonitoringStation objects"""
    #create empty set for rivers
    rivers = set()
    #iterate through stations
    for station in stations:
        #add rivers to set, only unique values are added to set
        rivers.add(station.river)
    return rivers

def stations_by_river(stations):
    """Returns a dictionary with rivers as keys and lists of stations as the values"""
    d = dict()
    #iterate through stations
    for station in stations:
        #if the river is already a key value, then add the station to the associated list
        if station.river in d:
            d[station.river].append(station)
        #otherwise add river as a new key and create the list, adding the associated station to it
        else:
            d[station.river] = [station,]
    return d