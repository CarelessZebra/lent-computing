"""unit test for flood module"""
from floodsystem.flood import stations_level_over_threshold
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import update_water_levels, build_station_list

def test_stations_level_over_threshold():
    """Test stations_levels_over_threshold function with various stations"""
    #build a station list with different water levels
    s1 = MonitoringStation("s1", "m1", "l1", (0,0), (0,1), "river", "town")
    s1.latest_level = -1
    s2 = MonitoringStation("s2", "m2", "l2", (0,0), (0,1), "river", "town")
    s2.latest_level = 0.5
    s3 = MonitoringStation("s3", "m3", "l3", (0,0), (0,1), "river", "town")
    s3.latest_level = 1.78
    s4 = MonitoringStation("s4", "m4", "l4", (0,0), (0,1), "river", "town")
    s4.latest_level = 0.600001

    stations = [s1, s2, s3, s4]
    #assert last two stations are only stations added to list and are sorted correctly
    assert(stations_level_over_threshold(stations, 0.6)==[(s3, 1.78), (s4, 0.600001)])

    #build list of the live data stations
    stations = build_station_list()
    #update water levels
    update_water_levels(stations)
    #assert that the relative water level for all the stations in the returned list is greater than the specified tolerance of 0.5
    for x in stations_level_over_threshold(stations, 0.5):
        assert(x[1]>=0.5)
