# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations


def run():
    """Requirements for Task 1F"""

    # Build list of stations
    stations = build_station_list()
    #create list of stations with inconsistent ranges
    inconsistent_list = inconsistent_typical_range_stations(stations)
    #change list so it just has the names of stations
    for i in range(0, len(inconsistent_list)):
        inconsistent_list[i] = inconsistent_list[i].name
    #sort list alphabetically
    inconsistent_list.sort()
    print(inconsistent_list)

   


if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
