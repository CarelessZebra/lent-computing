# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list

def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_typical_range_consistent():
    """Test the typical_range_consistent method for different ranges"""
     # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    river = "River X"
    town = "My Town"

    #reasonable range, should return true
    trange = (-2.3, 3.4445)
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    assert(s.typical_range_consistent()==True)

    #unreasonable range, should return False
    trange = (0, -74)
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    assert(s.typical_range_consistent()==False)

    #no data available, should return False
    trange = None
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    assert(s.typical_range_consistent()==False)

def test_inconsistent_typical_range_stations():
    """Test the function inconsistent_typical_range_stations from station.py"""
    # Build list of stations
    stations = build_station_list()
    #create list of inconsistent stations
    inc_list = inconsistent_typical_range_stations(stations)
    #check each station is inconsistent based on typical_range_consistent function
    for station in inc_list:
        assert(station.typical_range_consistent()==False)
    #make sure the number of inconsistent stations is 0 or more
    assert(len(inc_list)>=0)
    #make sure the number of inconsistent stations is less than the number of stations
    assert(len(inc_list)<=len(stations))

def test_relative_water_level():
    """Test the function relative_water_level from the MonitoringStation Class in station.py"""
    #create station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-1, 1)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    #testing for different typical range and latest level combinations
    s.latest_level = 0
    assert(s.relative_water_level() == 0.5)

    s.typical_range = (0, 1)
    s.latest_level = 0
    assert(s.relative_water_level() == 0)

    s.typical_range = (1, 5)
    s.latest_level = 0
    assert(s.relative_water_level() == -0.25)

