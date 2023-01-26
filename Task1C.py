# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    """Requirements for Task 1C"""
    #Build list of stations
    stations = build_station_list()

    #generate alphabetical leist of station names
    stations_in_r = []
    for station in stations_within_radius(stations, (52.2053, 0.1218), 10):
        stations_in_r.append(station.name)
    stations_in_r.sort()
    print(stations_in_r)


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
