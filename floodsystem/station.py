# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    def typical_range_consistent(self):
        """Finds if the data for typical ranges is consistent or unavailable, if it's inconsistent or unavailable returns False, otherwise returns True."""
        #return False if no data available
        if self.typical_range == None:
            return False
        #return false if typical high range is less than typical low range
        elif self.typical_range[1] < self.typical_range[0]:
            return False
        #if data is consistent returns True
        else:
            return True

def inconsistent_typical_range_stations(stations):
    """Given a list of stations, returns a list of stations with inconsistent ranges"""
    inconsistent_list = []
    #iterate through stations
    for station in stations:
        #add stations to list of stations with inconsistent ranges if their data is inconsistent
        if station.typical_range_consistent() == False:
            inconsistent_list.append(station)
    return inconsistent_list
