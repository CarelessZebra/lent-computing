# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

def run():
    """Requirements for Task 1D"""
    #Build list of stations
    stations = build_station_list()

    rivers = rivers_with_station(stations)
    print("---Number of rivers---")
    print(len(rivers))
    list_rivers = sorted(rivers)
    print("---List of first 10 rivers---")
    print(list_rivers[:10])

    d = stations_by_river(stations)

    print("---Stations on the Aire---")
    aire = d["River Aire"]
    for i in range(0, len(aire)):
        aire[i] = aire[i].name
    aire.sort()
    print(aire)
    
    print("---Stations on the Cam---")
    cam = d["River Cam"]
    for i in range(0, len(cam)):
        cam[i] = cam[i].name
    cam.sort()
    print(cam)

    print("---Stations on the Thames---")
    thames = d["River Thames"]
    for i in range(0, len(thames)):
        thames[i] = thames[i].name
    thames.sort()
    print(thames)

    

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
