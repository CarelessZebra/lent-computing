"""Unit test for the geo module"""
from floodsystem.geo import stations_within_radius, rivers_with_station, stations_by_river
from floodsystem.stationdata import build_station_list
from haversine import haversine

def test_stations_within_radius():
    """test stations_within_radius function"""
    #build a station list
    stations = build_station_list()

    #assert that every station is returned when using a massive distance
    s = stations_within_radius(stations, (0,0), 1000000)
    assert(len(s)==len(stations))
    #assert no stations are returned when radius is 0
    s = stations_within_radius(stations, (0,0), 0)
    assert(len(s)==0)

    #assert that every station within a radius 10 of (0,0) has a distance less than 10
    s = stations_within_radius(stations, (0,0), 10)
    for station in s:
        assert(haversine(station.coord, (0,0))<=10)

def test_rivers_with_station():
    """Test making list of unique rivers from stations"""
    #build a station list
    stations = build_station_list()

    rivers = rivers_with_station(stations)
    #make sure rivers are added to the list
    assert(len(rivers)>0)
    #assert there are less or equal rivers than stations
    assert(len(rivers)<=len(stations))

def test_stations_by_river():
    """Test station river dictionary creation function stations_by_river"""
    #build a station list
    stations = build_station_list()

    dictionary = stations_by_river(stations)
    #assert the number of keys in the dictionary equals the number of rivers
    assert(len(dictionary) == len(rivers_with_station(stations)))


