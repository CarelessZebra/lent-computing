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
    for station in stations:
        distance = haversine(station.coord, centre)
        if distance <= r:
            stations_in_radius.append(station)
    return stations_in_radius

def rivers_with_station(stations):
    """Builds and returns a set of unique rivers from a list of MonitoringStation objects"""
    rivers = set()
    for station in stations:
        rivers.add(station.river)
    return rivers

def stations_by_river(stations):
    """Returns a dictionary with rivers as keys and lists of stations as the values"""
    d = dict()
    for station in stations:
        if station.river in d:
            d[station.river].append(station)
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
