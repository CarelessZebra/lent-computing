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