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

def stations_by_distance(stations, p):
    D = {}
    E = {}
    L = []
    for station in stations:
        coord = station.coord
        dist = haversine(coord, p)
        L.append(dist)
        D[dist] = station.name
        E[dist] = station.town
    L.sort()
    T = []
    for i in L:
        T.append((D[i], E[i], i))
    return T

def rivers_by_station_number(stations, N):
    D = {}
    for station in stations:
        if station.river in D.keys():
            D[station.river] += 1
        else:
            D[station.river] = 0
    name = []
    num = []
    L = []
    for i in D.keys():
        name.append(i)
        num.append(D[i])
    for i in range(1, max(num) + 1):
        for j in range(len(num)):
            if num[j] == i:
                L.append((num[j], name[j]))
    L.reverse()
    K =[]
    n = 0
    for i in range(len(L)):
        if n < N-1:
            K.append(L[n])
            n += 1
        elif L[n][0] == L[i][0]:
            K.append(L[i])
    return((K))
